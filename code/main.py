import aioble
import bluetooth
import asyncio
import struct
from sys import exit
import utime
from picozero import RGBLED
from machine import Pin, PWM, ADC
from hitevent import HitEvent
# Import the MotorController class
from motor_class import MotorController
from basicgame import BasicGame
from virusgame import VirusGame
from discogame import DiscoGame
from wtfgame import WTFGame
from buzzer import Buzzer
from fireevent import FireEvent
from laser import Laser
from drivegame import DriveGame


laser = Laser(16)
photoresistor = ADC(28)
photoresistor_value = 0
## When calibrating what is the baseline
photoresistor_baseline_value = 0
photoresistor_hit_value = 28000
PHOTORES_HIT_FACTOR = 1.00
# After being hit you are immune for 2 seconds
HIT_DEBOUNCE_TIME = 2000

saved_sensitivity = 5

# RGB  status lights for indicating advertising, connected, and commands recieved.
rgb = RGBLED(red = 22, green = 21, blue = 20)

# ROVER_NAME needs to be a unique name for your rover.  It will be the advertised bluetooth device name
ROVER_NAME = "Put Your Unique Groovy Shark Name Here"

# Bluetooth parameters
BLE_NAME = f"{ROVER_NAME}"  # You can dynamically change this if you want unique names
BLE_SVC_UUID = bluetooth.UUID(0x181A)  # Environmental Sensing Service
BLE_CHARACTERISTIC_UUID = bluetooth.UUID(0x2A6E)  # Temperature
BLE_APPEARANCE = 0x0300  # Thermometer
BLE_ADVERTISING_INTERVAL = 2000

# Buzzer on pin 15
buzzer = Buzzer(15)

# Instantiate the motor controller
motor_controller = MotorController()

# Instantiate the HitEvent so it can be fired when hit:
hitevent = HitEvent()

# Instantiate the FireEvent so it can be emmitted when fire button is pressed:
fireevent = FireEvent()


## to select the game mode
def setGameMode(gamemode, motor_controller, rgb, laser, buzzer):
        if gamemode == "virus":
            print("Virus mode")
            return VirusGame(motor_controller, rgb, laser, buzzer)
        elif gamemode == "disco":
            print("Disco mode")
            return DiscoGame(motor_controller, rgb, laser, buzzer)
        elif gamemode == "hungry":
            print("Disco mode")
            # Return Hungry game impl
        elif gamemode == "wtf":
            print("WTF mode")
            return WTFGame(motor_controller, rgb, laser, buzzer)
        else:
            print("Default mode")
            return DriveGame(motor_controller, rgb, laser, buzzer)
    
def initializeGame(gamemode):
    global hitevent
    global laser
    global buzzer
    global fireevent
    
    # reset HitEvent to remove previous subscribers
    hitevent.reset()
    fireevent.reset()
    
    # get the game
    game = setGameMode(gamemode, motor_controller, rgb, laser, buzzer)

    # setup game
    game.setup()

    ## Set the method to be called when hitevent fires!
    hitevent.subscribe(game.onHit)
    fireevent.subscribe(game.onFire)



### Gets photoresistor value over and over again
### in an infinite loop sleeping a bit to yield
### control to other tasks.
### Calls "been_hit()" when photo_resistor_value exceeds the 
### photoresistor_hit_value
async def read_photo_resistor():
    global photoresistor_value 
    global hitevent
    # Keep track of when last hit
    hit_debounce_counter = utime.ticks_ms()
    print("reading photo res")
    while True:
        photoresistor_value = photoresistor.read_u16()
        if(photoresistor_value > photoresistor_hit_value):
            print("Got hit, photores value:" + str(photoresistor_value))
            current_time = utime.ticks_ms()
            # Calculate time passed since last hit
            time_passed = utime.ticks_diff(current_time,hit_debounce_counter)
            if (time_passed > HIT_DEBOUNCE_TIME):
                hitevent.fire()
                # Save time we were last hit
                hit_debounce_counter = utime.ticks_ms()
            else:
                print("no fire event because of debounce")
        
        await asyncio.sleep(0.01)  # Yield control to other tasks

### Set baseline for photores
def calibratePhotoRes():
    global photoresistor_baseline_value
    global saved_sensitivity
    # Get current value as a baseline
    photoresistor_baseline_value = photoresistor.read_u16()
    # set the sensitivity which sets the hit level
    setPhotoResSensitivity(saved_sensitivity)
    
## Set hit factor based on sensitivity value
def setPhotoResSensitivity(sensitivity_value):
    global saved_sensitivity
    # current calibrated baseline
    global photoresistor_baseline_value
    # current hit value
    global photoresistor_hit_value
    
    print("Setting sensitivity: Baseline photores value:" + str(photoresistor_baseline_value))
    # default hit factor to .20, 20%
    sensitivity_factor = .20
    # make sure sensitivity value is between 1 and 10
    if 1 <= sensitivity_value <= 10:
        sensitivity_factor = sensitivity_value * 0.08
    
    saved_sensitivity = sensitivity_value
    hit_factor = PHOTORES_HIT_FACTOR + sensitivity_factor
    print("hit factor:" + str(hit_factor))
    photoresistor_hit_value = photoresistor_baseline_value * hit_factor
    
    print("Photores HIT value:" + str(photoresistor_hit_value))

    
    
async def execute_command(command_with_data, characteristic):
    """ Control the remote control car based on the command received """
    
    if ':' in command_with_data:
        command, command_data = command_with_data.split(':', 1)
    else:
        command = command_with_data
        command_data = ""
    
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
    elif command == "game": ## TODO: change to whatever the game mode command is
        gamemode = command_data
        print("game mode = " + str(gamemode))
        initializeGame(gamemode)
    elif command == "fire":
        print("Fire dee lazzers!!")
        fireevent.fire()
    elif command == "calibrate":
        print("Calibrate Photores!!")
        calibratePhotoRes()
    elif command == "sensitivity":
        print("Set hit sensitivity!!")
        setPhotoResSensitivity(int(command_data))
    elif command == "trim":
        print("Set Trim!!")
        motor_controller.setTrim(int(command_data))
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
                await execute_command(command, characteristic)
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
            
            # Initialize game after connected - MODIFY THIS TO THE GAME MODE YOU WANT TO LAUNCH default
            initializeGame("default")
            tasks = [
                asyncio.create_task(receive_data_task(characteristic)),
            ]
            await asyncio.gather(*tasks)
            print(f"{ROVER_NAME} disconnected")
            break

async def main():
    global rgb
    global laser
    calibratePhotoRes()

    
    # Power on, turn red
    rgb.color = (255, 0, 0)
    # stop all motor activity
    motor_controller.stop()
    
    """ Main function """
    while True:        
        tasks = [
            asyncio.create_task(advertise_n_wait_for_connect()),
            asyncio.create_task(read_photo_resistor())
        ]
        await asyncio.gather(*tasks)

print("About to execute main")
asyncio.run(main())

