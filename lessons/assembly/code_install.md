# Install the Code

Open up Thonny and make sure the rover is turned off.  Always be sure to have the battery power off to the Pico before plugging in the USB cable.

Once the rover is switched off, plug in the USB cable.  If Thonny doesn't recognize the Pico, try hitting the STOP button.  If that doesn't work try clicking the bottom right to choose the correct device(MicroPyton on Pico).

When Thonny detects the Pico, copy the contents from [motor_class.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/motor_class.py) into a new/blank Thonny window.
Save this file onto the Pico as `motor_class.py`.

Now create a new Thonny tab(File->New) and copy the contents of [main.py](https://raw.githubusercontent.com/javaplus/MadScientist/refs/heads/main/code/main.py) into the new Thonny tab.
Now change the value of the ROVER_NAME variable to be something unique.  This will be the bluetooth advertised name of your Rover.  Change this to something you can easily remember and unique if doing this with a large group of others.
Below is the code you need to change... change the "sharkbot1" value to your special name:
```Python

# ROVER_NAME needs to be a unique name for your rover.  It will be the advertised bluetooth device name
ROVER_NAME = "sharkbot1"

```

After changing the ROVER_NAME value, save the code to the Pico as `main.py`. 

**Fun Fact**: any code you save into `main.py` at the root of the Pico will run automatically when it's powered up.

After saving the `main.py` and `motor_class.py` to the Pico, make sure to have the main.py window up in Thonny and click the "Run" button.  See if there are any errors in the Shell.
If you see an error about a picozero library or module, be sure to follow these steps to [install picozero onto the Pico](https://picozero.readthedocs.io/en/latest/gettingstarted.html#install-picozero-from-pypi-in-thonny).

If you see no errors, try to use the mad scientist app to connect to the Rover.  Be sure to keep the power switch off on the Rover.  
When the RGB eyes are flashing blue, that means the rover is advertising and waiting for a bluetooth connection.  
In the mad scientist app, type in the value you put for the ROVER_NAME variable to make it easier to find your rover and then hit `CONNECT`.

