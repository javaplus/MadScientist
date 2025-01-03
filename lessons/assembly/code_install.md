# Install the Code

Open up Thonny and make sure the **rover is turned off**.  Always be sure to have the battery power off to the Pico before plugging in the USB cable.

Once the rover is switched off, plug in the USB cable.  If Thonny doesn't recognize the Pico, try hitting the STOP button.  If that doesn't work try clicking the bottom right to choose the correct device : MicroPyton(Raspberry Pi Pico).

#### Motor Class

When Thonny detects the Pico, copy the contents from [motor_class.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/motor_class.py) into a new/blank Thonny window (File->New).
Save this file onto the Pico as `motor_class.py`.

#### Hit Event  
Now create a new Thonny tab(File->New) and copy the contents of [hitevent.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/hitevent.py) into the new Thonny tab.  
Save this file onto the Pico as `hitevent.py`.

#### Basic Game  
Now create a new Thonny tab and copy the contents of [basicgame.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/basicgame.py) into the new Thonny tab.  
Save this file onto the Pico as `basicgame.py`.

#### Main

Now create a new Thonny tab(File->New) and copy the contents of [main.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/main.py) into the new Thonny tab.
Now change the value of the `ROVER_NAME` variable to be something unique.  This will be the bluetooth advertised name of your Rover.  Change this to something you can easily remember and unique if doing this with a large group of others.
Below is the code you need to change... change the "sharkbot1" value to your special name:
```Python

# ROVER_NAME needs to be a unique name for your rover.  It will be the advertised bluetooth device name
ROVER_NAME = "sharkbot1"

```
After changing the ROVER_NAME value, save the code to the Pico as `main.py`. 

**Fun Fact**: any code you save into `main.py` at the root of the Pico will run automatically when it's powered up.

####  Try It Out!

After saving the `motor_class.py`, `hitevent.py`, `basicgame.py`, and `main.py` to the Pico, make sure to have the `main.py` window up in Thonny and click the "Run" button.  See if there are any errors in the Shell.
If you see an error about a **picozero** library or module, be sure to follow these steps to [install picozero onto the Pico](https://picozero.readthedocs.io/en/latest/gettingstarted.html#install-picozero-from-pypi-in-thonny).

If you there are no errors, it's time to test it out!

Since testing it out means using the mad scientist app to control the motors, you may want to lift the Rover off the ground while connected to the USB cable.  You can use one of the included clear dixie cups upside down under the Rover to keep the tracks off the ground.

![Rover Lift](/lessons/images/assembly/lift.jpg)
 Now open the mad scientist app and connect to the Rover.  Be sure to keep the power switch off on the Rover.  

When the RGB eyes are flashing blue, that means the rover is advertising and waiting for a bluetooth connection.  
In the mad scientist app, type in the value you put for the `ROVER_NAME` variable to make it easier to find your rover and then hit `CONNECT`.

When the app is connected to the Rover, the eyes should turn green.  Now try to move the joystick in the app to test the motor control is working.  If any of the movement is reversed, you can simply go to the settings menu of the app and reverse the controls.

#### FREEDOM!!!

If everything tests out ok while connected via the USB cable, it's time to  unplug the USB cable and set it free.  Place the Rover on the ground and turn the power switch on.  The eyes should flash blue again showing that it's advertising and ready to connect.  Use the app again to connect and try it out!!!

