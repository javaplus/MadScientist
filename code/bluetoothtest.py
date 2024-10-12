import aioble
import bluetooth
import asyncio
import struct
from sys import exit

# Define UUIDs for the service and characteristic
# NOT USED??? _SERVICE_UUID = bluetooth.UUID(0x1848) #Media Control Service 
# NOT USED??? _CHARACTERISTIC_UUID = bluetooth.UUID(0x2A6E)

# IAM = "Central" # Change to 'Peripheral' or 'Central'
#IAM = "Central"
IAM = "Peripheral"

if IAM not in ['Peripheral','Central']:
    print("IAM must be either Peripheral or Central")
    exit()

if IAM == "Central":
    IAM_SENDING_TO = "Peripheral"
else:
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

# def encode_message(message):
#     """ Encode a message to bytes """
#     return message.encode('utf-8')

def decode_message(message):
    """ Decode a message from bytes """
    return message.decode('utf-8')

# async def send_data_task(connection, characteristic):
#     """ Send data to the connected device """
#     global message_count
#     while True:
#         if not connection:
#             print("error - no connection in send data")
#             continue

#         if not characteristic:
#             print("error no characteristic provided in send data")
#             continue

#         message = f"{MESSAGE} {message_count}"
#         message_count +=1
#         print(f"sending {message}")

#         try:
#             msg = encode_message(message)
#             characteristic.write(msg)

#             await asyncio.sleep(0.5)
#             response = decode_message(characteristic.read())

#             print(f"{IAM} sent: {message}, response {response}")
#         except Exception as e:
#             print(f"writing error {e}")
#             continue

#         await asyncio.sleep(0.5)

async def receive_data_task(characteristic):
    """ Receive data from the connected device """
    global message_count
    print("Trying to read data!");
    while True:
        try:
            # data = await characteristic.read()
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
