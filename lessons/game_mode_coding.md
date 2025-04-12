# Programming New Game Modes

## Overview
Game modes really come down controlling what happens when you get hit, motor speed, what to do when you fire, and what sounds to make when.

## Base Class
To implement a new game mode, you need to create a new class that extends/implements the [`BaseGame` class](https://github.com/javaplus/MadScientist/blob/3be6801566cf3852717db674f972e4c576ec4078/code/basegame.py#L3).

```Python

from motor_class import MotorController

class BaseGame:
    # Constructor gets motor_controller and rgb
    def __init__(self, motor_controller, rgb, laser, buzzer):
        self.motor_controller = motor_controller
        self.rgb = rgb
        self.laser = laser
        self.buzzer = buzzer


    ## Implement Setup (initialize rgbs and motor status)
    def setup(self):
        pass

    ## implement on Hit.
    def onHit(self):
       pass
   
    ## implement on Fire.
    def onFire(self):
       pass

```

## Custom Game Class

When you extend this class you get the constructor by default which takes in the `motor_controller`, the `rgb`, buzzer, and the `laser`.

These are the 4 things with the current hardware you can control.

Here's an example of how to extend it with a simple implementation:

```Python
from basegame import BaseGame
from laser import Laser
from motor_class import MotorController

class BasicGame(BaseGame):

    ## Implement Setup
    def setup(self):
        # set color to green
        self.rgb.color = (0, 255, 0)
        self.laser.turnOn()

    ## implement on Hit.
    def onHit(self):
        print("Basic Game been hit!!")
        # Let's flash our eyes
        # go red
        self.rgb.color = (255, 0, 0)
        self.motor_controller.spin_lock()
        self.laser.turnOff()
    
```

Notice that there is no need to create a constructor when you implement the `BaseGame` class as you inherit its constructor.

This `BasicGame` class simply sets the color to green on setup.

The `onHit()` function simply changes the color to red and then causes the motor to do a `spin_lock`, which is basically just a forced spin for a certain amount of time.

## How the Game Class is used

The `setup()` function gets called as soon as the game mode is changed or initiated.
Currently, the game mode can change based on the command from the bluetooth remote app.
In [main.py](/code/main.py), the `execute_command()` function has an `if` block to set the game mode. The `initializeGame()` function takes in the game mode string to determine what game mode to use by calling the `setGameMode()` function (also in `main.py`) that will instantiate the appropriate game class and return it.  

Here is the `initializeGame()` function(NOTE: This is for informational purposes, you should not have to change this function for your own game class):

```Python
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

```

Notice the `initializeGame()` function resets the game events. Currently there's only `hitevent` and `fireevent`.
It also then subscribes the game class returned by `setGameMode()` to the `hitevent` and `fireevent`.  This allows the game class's `onHit()` function to be called when there is a hit detected. And the `onFire()` function of your game class to be called with the fire button is pressed.

Let's look at the `setGameMode()` function now:

```Python

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
```

This function is a simple `if`/`else` block that instantiates the correct game class to return based on the `gamemode` parameter.  This is where you would instantiate your custom game mode.

If this `setGameMode()` returns your custom game class instance, then it will have its `setup()` function called almost immediately, and its `onHit()` function will be called whenever it gets hit and `onFire()` will be called when the fire button is pressed.

### What you have to change

So, to implement your own game mode, you need to:
1) Create your own class that extends the `BaseGame` class
2) Update the `setGameMode()` to instantiate your class and return it.

For instantiating your game mode, you will most likely have to replace an existing game mode in the `setGameMode()` function.  Or make it the new default and return it in the final `else` block.

### Enhancements

To make things more interesting you may want to implement new methods on the `MotorController` class in [motor_class.py](/code/motor_class.py) or Buzzer class that you can call in your `onHit()` function.


