import aioble
import bluetooth
import asyncio
import struct
from sys import exit

# IAM = "Central" # Change to 'Peripheral' or 'Central'
IAM = "Peripheral"
IAM_SENDING_TO = "Central"

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

def decode_message(message):
    """ Decode a message from bytes """
    return message.decode('utf-8')

async def control_car(command):
    """ Control the remote control car based on the command received """
    if command in COMMANDS:
        print(COMMANDS[command])
        # Here you would add code to control the actual car hardware
    else:
        print("Unknown command")

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
                await control_car(command)

            message_count += 1

        except asyncio.TimeoutError:
            print("Timeout waiting for data.")
            break
        except Exception as e:
            print(f"Error receiving data: {e}")
            break

async def run_peripheral_mode():
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

    while True:
        async with await aioble.advertise(
            BLE_ADVERTISING_INTERVAL,
            name=BLE_NAME,
            services=[BLE_SVC_UUID],
            appearance=BLE_APPEARANCE) as connection:
            print(f"{BLE_NAME} connected to another device: {connection.device}")

            tasks = [
                asyncio.create_task(receive_data_task(characteristic)),
            ]
            await asyncio.gather(*tasks)
            print(f"{IAM} disconnected")
            break

async def main():
    """ Main function """
    while True:
        print("I'm peripheral")
        tasks = [
            asyncio.create_task(run_peripheral_mode()),
        ]
        await asyncio.gather(*tasks)

asyncio.run(main())
