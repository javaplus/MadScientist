import aioble
import bluetooth
import asyncio
import struct
from sys import exit

# IAM = "Central" # Change to 'Peripheral' or 'Central'
#IAM = "Central"
IAM = "Peripheral"
IAM_SENDING_TO = "Central"

MESSAGE = f"Hello from {IAM}!"

# Bluetooth parameters
BLE_NAME = f"{IAM}"  # You can dynamically change this if you want unique names
#BLE_SVC_UUID = bluetooth.UUID(0x181A)
BLE_SVC_UUID = bluetooth.UUID(0x181A) #Environmental Sensing Service
#BLE_CHARACTERISTIC_UUID = bluetooth.UUID(0x2A6E)
BLE_CHARACTERISTIC_UUID = bluetooth.UUID(0x2A6E) #Temperature
BLE_APPEARANCE = 0x0300 # Thermometer
BLE_ADVERTISING_INTERVAL = 2000
BLE_SCAN_LENGTH = 5000
BLE_INTERVAL = 30000
BLE_WINDOW = 30000

# state variables
message_count = 0

def decode_message(message):
    """ Decode a message from bytes """
    return message.decode('utf-8')

async def receive_data_task(characteristic):
    """ Receive data from the connected device """
    global message_count
    print("Trying to read data!");
    while True:
        try:
            # data = await characteristic.read()
            # not sure why written() works and read does not??
            connection, data = await characteristic.written()

            if data:
                print(f"{IAM} received: {decode_message(data)}, count: {message_count}")
                # await characteristic.write(encode_message("Got it"))
                await asyncio.sleep(0.5)

            message_count += 1

        except asyncio.TimeoutError:
            print("Timeout waiting for data in {ble_name}.")
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
