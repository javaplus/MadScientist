# Install the Code

Open up Thonny and make sure the **rover is turned off**.  Always be sure to have the battery power off to the Pico before plugging in the USB cable.

Once the rover is switched off, plug in the USB cable.  If Thonny doesn't recognize the Pico, try hitting the STOP button.  If that doesn't work try clicking the bottom right to choose the correct device : MicroPython(Raspberry Pi Pico).


#### Main

Create a new Thonny tab (File->New) and copy the contents of [main.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/main.py) into it.
Change the value of the `ROVER_NAME` variable to be something unique.  This will be the Bluetooth device name of your Rover.  Change this to something you can easily remember and unique if doing this with a large group of others.
Below is the code you need to change... change the "sharkbot1" value to your special name:
```Python

# ROVER_NAME needs to be a unique name for your rover.  It will be the Bluetooth device name
ROVER_NAME = "sharkbot1"

```
After changing the ROVER_NAME value, save the code to the Pico as `main.py`. 

**Fun Fact**: any code you save into `main.py` at the root of the Pico will run automatically when it's powered up.

#### Base Game  
Create a new Thonny tab and copy the contents of [basegame.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/basegame.py) into it.  
Save this file onto the Pico as `basegame.py`.


#### Basic Game  
Create a new Thonny tab and copy the contents of [basicgame.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/basicgame.py) into it.  
Save this file onto the Pico as `basicgame.py`.

#### Buzzer  
Create a new Thonny tab and copy the contents of [buzzer.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/buzzer.py) into it.  
Save this file onto the Pico as `buzzer.py`.

#### Event  
Create a new Thonny tab and copy the contents of [event.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/event.py) into it.  
Save this file onto the Pico as `event.py`.

#### FireEvent  
Create a new Thonny tab and copy the contents of [fireevent.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/fireevent.py) into it.  
Save this file onto the Pico as `fireevent.py`.

#### Hit Event  
Create a new Thonny tab (File->New) and copy the contents of [hitevent.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/hitevent.py) into it.  
Save this file onto the Pico as `hitevent.py`.

#### Laser  
Create a new Thonny tab (File->New) and copy the contents of [laser.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/laser.py) into it.  
Save this file onto the Pico as `laser.py`.

#### Motor Class
When Thonny detects the Pico, copy the contents from [motor_class.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/motor_class.py) into a new/blank Thonny window (File->New).
Save this file onto the Pico as `motor_class.py`.  

#### Virus Game  
Create a new Thonny tab and copy the contents of [virusgame.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/virusgame.py) into it.  
Save this file onto the Pico as `virusgame.py`.

####  Try It Out!

After saving all these files to the Pico, make sure to have the `main.py` window up in Thonny and click the "Run" button.  See if there are any errors in the shell.
If you see an error about a **picozero** library or module, be sure to follow these steps to [install picozero onto the Pico](https://picozero.readthedocs.io/en/latest/gettingstarted.html#install-picozero-from-pypi-in-thonny).

If there are no errors, it's time to test it out!

Since testing it out means using the mad scientist app to control the motors, you may want to lift the Rover off the ground while connected to the USB cable.  You can use one of the included clear dixie cups upside down under the Rover to keep the tracks off the ground.

<img alt="Rover Lift" src="/lessons/images/assembly/lift.jpg" width="500"/>
Now open the mad scientist app and connect to the Rover.  Be sure to keep the power switch off on the Rover.  

When the RGB eyes are flashing blue, that means the rover is advertising and waiting for a Bluetooth connection.  
In the mad scientist app, type in the value you put for the `ROVER_NAME` variable to make it easier to find your rover and then hit `CONNECT`.

When the app is connected to the Rover, the eyes should turn green.  Now try to move the joystick in the app to test the motor control is working.  If any of the movement is reversed, you can simply go to the settings menu of the app and reverse the controls.

#### FREEDOM!!!

If everything tests out ok while connected via the USB cable, it's time to unplug the USB cable and set it free.  Place the Rover on the ground and turn the power switch on.  The eyes should flash blue again, showing that it's advertising and ready to connect.  Use the app again to connect and try it out!!!

