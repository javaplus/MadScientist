# Programming New Game Modes

## Overview
Game modes really come down to what color should your RGB be and what should happen when you get hit.

## Base Class
To implement a new game mode, you need to create a new class that extends/implements the [BaseGame class](https://github.com/javaplus/MadScientist/blob/3be6801566cf3852717db674f972e4c576ec4078/code/basegame.py#L3).

```Python
from motor_class import MotorController

class BaseGame:
    # Constructor gets motor_controller and rgb
    def __init__(self, motor_controller, rgb, laser):
        self.motor_controller = motor_controller
        self.rgb = rgb
        self.laser = laser


    ## Implement Setup (initialize rgbs and motor status)
    def setup(self):
        pass

    ## implement on Hit.
    def onHit(self):
       pass
    

```

## Custom Game Class

When you extend this class you get the constructor by default which takes in the motor_controller, the rgb, and the laser.

These are the three things with the current hardware you can control.

Here's an example of how to extend it with a simple implementation:

```Python
from basegame import BaseGame
from motor_class import MotorController

class BasicGame(BaseGame):

    ## Implement Setup
    def setup(self):
        # set color to green
        self.rgb.color = (0, 255, 0)

    ## implement on Hit.
    def onHit(self):
        print("Basic Game been hit!!")
        # go red
        self.rgb.color = (255, 0, 0)
        self.motor_controller.spin_lock()
    
```

Notice there is no need to create a constructor when you implement the BaseGame class as you inherit it's constructor.

This BasicGame class simply sets the color to green on setup.

The `onHit()` function simply changes the color to red and then causes the motor to do a spin_lock, which is basically just a forced spin for a certain amount of time.


## How the Game Class is used

The `setup()` function gets called as soon as the game mode is changed or initiated.
Currently, the game mode can change based on the command from the bluetooth remote app.
In the [main.py](/code/main.py), the `execute_command()` function has an if block to set the game mode. The `initializeGame()` function takes in the game mode string to determine what game mode to use by calling the `setGameMode()` function (also in `main.py`) that will instantiate the appropriate game class and return it.

Here is the `initializeGame()` function:

```Python
def initializeGame(gamemode):
    global hitevent
    
    # reset HitEvent to remove previous subscribers
    hitevent.reset()
    
    # get the game
    game = setGameMode(gamemode, motor_controller, rgb)

    # setup game
    game.setup()

    ## Set the method to be called when hitevent fires!
    hitevent.subscribe(game.onHit)

```

Notice the `initializeGame()` function resets the game events. Currently there's only `hitevent`.
It also, then subscribes the game class returned by `setGameMode()` to the `hitevent`.  This allows the game class's `onHit()` function to be called when there is a hit detected.

Let's look at the `setGameMode()` function now:

```Python

## to select the game mode
def setGameMode(gamemode, motor_controller, rgb, laser):
        if gamemode == "Virus":
            print("Virus mode")
            # Return VirusGame impl
        elif gamemode == "Disco":
            print("Disco mode")
            # Return Disco Game impl
        elif gamemode == "Hungry":
            print("Disco mode")
            # Return Hungry game impl
        elif gamemode == "WTF":
            print("WTF mode")
            # Return whatever WTF mode is
        else:
            print("Default mode")
            return BasicGame(motor_controller, rgb, laser)

```

This function is a simple if/else block that instantiates the correct game class to return based on the `gamemode` parameter.  This is where you would instantiate your custom game mode.

If this `setGameMode()` returns your custom game class instance, then it will then have it's `setup()` function called almost immediately and then it's `onHit()` function will be called whenever it gets hit.

### What all do you have to change

So, to implement your own game mode, you need to :
1) Create your own class that extends the BaseGame class
2) Update the `setGameMode()` to instantiate your class and return it.

For instantiating your game mode, you will most likely have to replace an existing game mode in the `setGameMode()` function.  Or make it the new default and return it in the final else block.

### Enhancements

To make things more interesting you may want to implement new methods on the `MotorController` class in the [motor_class.py](/code/motor_class.py) that you can call in your `onHit()` function.

Another future enhancement could be to add a fireevent copying the hitevent pattern to be able to do something when the fire button is hit. (Fire button may be coming soon to the mad scientist app).

