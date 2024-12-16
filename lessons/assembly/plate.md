# Pico Plate & Motor Controller


### Pico Installation

Take your pico plate (the flattish square piece) and your Pico W. On the pico plate, you should see a small square in the corner to hold the motor controller.  Orient the plate so that square is in the bottom left.  

TODO: PICO Plate with motor controller square bottom left


Turn the Pico so your pins are sticking up in the air and the usb jack is pointing away from you.  Now, place the Pico W on the for raised pedestals on the plate that should align with the four holes in the Pico.  

TODO: Pico plate with pico on it no pegs


You should have 4 small plastic pegs about .25 inches long. Take your pegs and push them partially through the holes of the Pico and into the holes in the pedestals. Push the pegs about half way down into the plate leaving a little gap so you can still raise the Pico a bit to route wires underneath it.  

TODO: Pico plate with pico on it and pegs partially installed



### Motor Controller

#### Mount the Motor Controller
Now take the motor controller and put it into the bottom left square on the pico plate  so that the 4 lone pins that stick downward can fit through the bottom slot on the far bottom left of the recessed square. It's easiest to align the downward 4 pins through the hole and then angle the motor controller so the side closest to bottom goes in last. So, the sidee with the pin marked INT4 should go in first and then the part of the motor controller at the bottom should snap in last.  The motor controller should snap in securely into the recessed square and the top of the red part of the motor controller should be slightly lower than the top surface of the plate.

![Motor Controller install](/lessons/images/assembly/motor_controller_install.jpg)

**NOTE**: Ignore the wires and pico in the picture below, it's just to show you the way the motor controller should fit in.
![Pico Bottom](/lessons/images/assembly/pico_plate_bottom.jpg)


#### Wire the Motor Controller

Take 4 5cm female to female wires (recommend a combination of blue,yellow, green is fine) and fish them under the pico so that the female ends are on opposite sides of the Pico. Go ahead and grab a black or white 5cm female to female wire as well. Now connect on end of the wires the Int1, Int2, Int3, and Int4 pins that stick up from the motor controller.  The color of the wires don't matter, but it would be beneficial to have different colors for every other pin. Now you will connect the other end of the wires to the GPIO pins on the Pico.  You will be connecting them to GP10 throuh GP13.  The important part is that you connect INT1 and INT2 to GP12 and GP13 and INT3 and INT4 to GP10 and GP11.  When it comes time to test the motor function, you may need to switch wires around to get the RVR to move in the intended function.

![Colored wires](/lessons/images/assembly/motor_controller_wires.jpg)

**NOTE:** These pics show the black ground wire as well, you'll run that in the next step. For now just run the four colored wires.
![Pico Motor Controller Wires topdown](/lessons/images/assembly/pico_plate_motor_controller_topdown.jpg)

![Pico Motor Controller Wires Ran Close up](/lessons/images/assembly/pico_plate_motor_controller_closeup.jpg)


Now take the black or white 5cm female to female jumper wire and route it under the Pico like the 4 colored wires.  This wire will connect the (-) on the motor controller to a ground on the Pico.  We find the ground wire that is 3 down from the top right is best for this due to wire management. 

![Pico Motor Controller Wires Ran](/lessons/images/assembly/pico_plate_motor_controller_closeup_usb.jpg)

At this point, the motor controller is just missing a cable to it's (+) positive terminal and the 4 Motor pins on the bottom are unconnected.  We will connect those when we put the plate on the chassis.
Now, you can press the 4 pegs that hold the Pico down fully down into place to more securely hold the Pico.  Don't use a ton of force and don't worry if they don't go all the way in.  They just need to keep the Pico from moving around or coming off the plate.


