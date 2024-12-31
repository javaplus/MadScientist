import aioble
import bluetooth
import asyncio
import struct
from sys import exit
import utime
from picozero import RGBLED
from machine import Pin, PWM, ADC

laser = Pin(16, Pin.OUT)

photoresistor = ADC(28)
photoresistor_value = 0
photoresistor_hit_value = 28000

# RGB  status lights for indicating advertising, connected, and commands recieved.
rgb = RGBLED(red = 22, green = 21, blue = 20)

# ROVER_NAME needs to be a unique name for your rover.  It will be the advertised bluetooth device name
ROVER_NAME = "sharkbot1"
MESSAGE = f"Hello from {ROVER_NAME}!"

# Bluetooth parameters
BLE_NAME = f"{ROVER_NAME}"  # You can dynamically change this if you want unique names
BLE_SVC_UUID = bluetooth.UUID(0x181A)  # Environmental Sensing Service
BLE_CHARACTERISTIC_UUID = bluetooth.UUID(0x2A6E)  # Temperature
BLE_APPEARANCE = 0x0300  # Thermometer
BLE_ADVERTISING_INTERVAL = 2000

# Import the MotorController class
from motor_class import MotorController  # Adjust import as necessary

# Instantiate the motor controller
motor_controller = MotorController()

### Gets photo resistor value over and over again
### in an infinite loop sleeping a bit to yield
### control to other tasks.
### Calls "been_hit()" when photo_resistor_value exceeds the 
### photoresistor_hit_value
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
    motor_controller.spin_lock()
        
    
async def control_car(command_with_data, characteristic):
    """ Control the remote control car based on the command received """

    command, command_data = command_with_data.split(':', 1)
    print(f"Received command:{command}     data:{command_data}")

    if command == "move":
        move_directions = command_data.split(',')
        if len(move_directions) >= 2:
            motor_controller.move(float(move_directions[0]), float(move_directions[1]))
        else:            
            print(f"Invalid move command {move_directions}")
    elif command == "rgb":
        print(f"Setting RGB to {command_data}")
        rgb.color = tuple(map(int, command_data.split(',')))
    elif command == "stop":
        motor_controller.stop()
    else:
        print("Unknown command")
        response_message = "Unknown command received."
        await characteristic.write(response_message.encode('utf-8'))
async def receive_data_task(characteristic):
    """ Receive data from the connected device """
    print("Waiting for commands...")
    while True:
        try:
            connection, data = await characteristic.written()
            if data:
                command = data.decode('utf-8')
                await control_car(command, characteristic)
        except asyncio.TimeoutError:
            print("Timeout waiting for data.")
            break
        except Exception as e:
            print(f"Error receiving data: {e}")
            

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
        # advertising on, blink blue
        rgb.blink(colors=[(0, 0, 255),(0, 0, 0)])
        async with await aioble.advertise(
            BLE_ADVERTISING_INTERVAL,
            name=BLE_NAME,
            services=[BLE_SVC_UUID],
            appearance=BLE_APPEARANCE) as connection: # type: ignore
            print(f"{BLE_NAME} connected to another device: {connection.device}")
            
            # connected turn green
            rgb.color = (0, 255, 0)

            tasks = [
                asyncio.create_task(receive_data_task(characteristic)),
            ]
            await asyncio.gather(*tasks)
            print(f"{ROVER_NAME} disconnected")
            break

async def main():
    global rgb
    global laser
    # Power on, turn red
    rgb.color = (255, 0, 0)
    # stop all motor activity
    motor_controller.stop()
    # turn on laser
    laser.value(1)
    """ Main function """
    while True:        
        tasks = [
            asyncio.create_task(advertise_n_wait_for_connect()),
            asyncio.create_task(read_photo_resistor())
        ]
        await asyncio.gather(*tasks)

print("About to execute main")
asyncio.run(main())

