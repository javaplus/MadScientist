import aioble
import bluetooth
import asyncio
import struct
from sys import exit
import utime
from picozero import RGBLED
from machine import Pin, PWM, ADC


laser = Pin(16, Pin.OUT)

photoresistor = machine.ADC(28)
photoresistor_value = 0
photoresistor_hit_value = 28000

# RGB  status lights for indicating advertising, connected, and commands recieved.
rgb = RGBLED(red = 22, green = 21, blue = 20)

# IAM = "Central" # Change to 'Peripheral' or 'Central'
IAM = "Peripheral"

MESSAGE = f"Hello from {IAM}!"

# Bluetooth parameters
BLE_NAME = f"{IAM}"  # You can dynamically change this if you want unique names
BLE_SVC_UUID = bluetooth.UUID(0x181A)  # Environmental Sensing Service
BLE_CHARACTERISTIC_UUID = bluetooth.UUID(0x2A6E)  # Temperature
BLE_APPEARANCE = 0x0300  # Thermometer
BLE_ADVERTISING_INTERVAL = 2000

# Define commands for the remote control car
COMMANDS = {
    "forward": "Moving forward",
    "backward": "Moving backward",
    "left": "Turning left",
    "right": "Turning right",
    "stop": "Stopping"
}

# state variables
message_count = 0

# Import the MotorController class
from motor_class import MotorController  # Adjust import as necessary

# Instantiate the motor controller
motor_controller = MotorController()

def decode_message(message):
    """ Decode a message from bytes """
    return message.decode('utf-8')

def encode_message(message):
    """ Encode a message to bytes """
    return message.encode('utf-8')

async def read_photo_resistor():
    global photoresistor_value 
    print("reading photo res")
    while True:
        photoresistor_value = photoresistor.read_u16()
        if(photoresistor_value > photoresistor_hit_value):
              await been_hit()
        await asyncio.sleep(0.01)  # Yield control to other tasks
    
async def been_hit():
    global rgb
    print("I've been hit!!")
    # Let's flash our eyes
    # go red
    rgb.color = (255, 0, 0)
    # sleep for a second
    utime.sleep_ms(1000)
    # go green
    rgb.color = (0, 255, 0)
        
        
     
    
    
async def control_car(command, characteristic):
    """ Control the remote control car based on the command received """
    if command in COMMANDS:
        action_message = COMMANDS[command]
        print(action_message)

        print(f"command is:{command}")
        print(command == "forward")
        # Control the motors based on the command
        if command == "forward":
            print("calling motor controller for forward")
            motor_controller.change_speed_and_direction("forward")
        elif command == "backward":
            motor_controller.change_speed_and_direction("backward")
        elif command == "left":
            motor_controller.change_speed_and_direction("left")
        elif command == "right":
            motor_controller.change_speed_and_direction("right")
        elif command == "stop":
            motor_controller.stop()

        response_message = "Got it"
        print(f"response message = {response_message}")

        # Send response back to the Central
        try:
            encoded_message = encode_message(response_message)
            # await characteristic.write(encoded_message)
            print("NOT sending response")
        except Exception as e:
            print(f"Error writing response: {e}")
    else:
        print("Unknown command")
        response_message = "Unknown command received."
        
        # Send response back to the Central
        await characteristic.write(encode_message(response_message))

async def receive_data_task(characteristic):
    """ Receive data from the connected device """
    global message_count
    print("Waiting for commands...")
    while True:
        try:
            
            connection, data = await characteristic.written()

            if data:
                command = decode_message(data)
                print(f"{IAM} received command: {command}, count: {message_count}")
                await control_car(command, characteristic)
            

        except asyncio.TimeoutError:
            print("Timeout waiting for data.")
            break
        except Exception as e:
            print(f"Error receiving data: {e}")
            break

async def advertise_n_wait_for_connect():
    """ Run the peripheral mode """
    # Set up the Bluetooth service and characteristic
    ble_service = aioble.Service(BLE_SVC_UUID)
    characteristic = aioble.Characteristic(
        ble_service,
        BLE_CHARACTERISTIC_UUID,
        read=True,
        notify=True,
        write=True,
        capture=True,
    )
    aioble.register_services(ble_service)

    print(f"{BLE_NAME} starting to advertise")
    global rgb
    while True:
        # advertising on, turn blue
        rgb.color = (0, 0, 255)
        async with await aioble.advertise(
            BLE_ADVERTISING_INTERVAL,
            name=BLE_NAME,
            services=[BLE_SVC_UUID],
            appearance=BLE_APPEARANCE) as connection:
            print(f"{BLE_NAME} connected to another device: {connection.device}")
            
            # connected turn green
            rgb.color = (0, 255, 0)

            tasks = [
                asyncio.create_task(receive_data_task(characteristic)),
            ]
            await asyncio.gather(*tasks)
            print(f"{IAM} disconnected")
            break

async def main():
    global rgb
    global laser
    # Power on, turn red
    rgb.color = (255, 0, 0)
    # turn on laser
    laser.value(1)
    
    """ Main function """
    while True:
        print("I'm peripheral")
        
        tasks = [
            asyncio.create_task(advertise_n_wait_for_connect()),
            asyncio.create_task(read_photo_resistor())
        ]
        await asyncio.gather(*tasks)

print("About to execute main")
asyncio.run(main())
