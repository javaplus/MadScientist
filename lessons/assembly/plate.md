# Pico Plate & Motor Controller


## Parts

- Pico WH  
- 4 x 10cm female to female wires (recommend a combination of blue, yellow, white, and green)

***Pico WH and wires(Note colors may be different than pictured)**
<img alt="Pico Plate Parts" src="../images/assembly/v3/Pico_Wire_Parts.jpg" width="500"/>

## Prepare Pico Wires for Motor Controller

We are now going to connect our 4 wires to the Pico that will eventually connect to the motor controller that will allow the Pico to control our motors.

Your 4 wires will go on the GPIO pins GP10, GP11, GP12, and GP13.
<details>
	<summary>More Details</summary>

	The exact color of the wires doesn't matter, but it may be easier to follow the pictures. The wires go together in pairs to control the 2 motors. The GP10 and 11 pins control one motor by going to the Motor Controller's INT3 and INT4. While the GP12 and 13 pins on the Pico need to connect to the INT1 and INT2 pins. 

</details>

Take your 4 wires and connect them to the Pico as indicated in the picture below.

<img alt="Pico wires for Motor Controller" src="../images/assembly/v3/Pico_Wiring_1.jpg" width="500"/>

Now your Pico wires are ready to connect to the motor controller, but let's mount the motor controller to the plate first.


## Motor Controller Install

### Parts
Grab the Pico plate (the flattish square piece) and your motor controller.

Orient the plate so that the square is in the bottom left as seen below.

<img alt="Pico Plate and Motor Controller parts" src="../images/assembly/v3/Motor_Controller_Plate_Parts.jpg" width="500" />


### Mount the Motor Controller

Take the motor controller and put it into the bottom left square on the Pico plate so that the 4 pins on the left side of the motor controller go through the slot on the left of the recessed square.  The 6 pins of the motor controller should be facing up and on the right side of the recessed square. To snap the motor controller in the recessed slot, align the downward 4 pins through the hole, and then angle the motor controller so that the side opposite the capacitors (the round silver things) goes in the recess first. Then the side with the capacitors; which are closest to the bottom edge and closest to you in the picture, will go in last.

<img alt="Motor Controller angled" src="../images/assembly/v3/MC_In_Plate1.jpg" width="500"/>

Using your thumbs on top of the capacitors, snap the motor controller securely into the recessed square. It will take a little force, but you should be able to feel a satisfying snap when it goes in place.

<img alt="Motor Controller Snap with thumbs" src="../images/assembly/v3/MC_In_Plate2.jpg" width="500"/>

The top of the red part of the motor controller should be slightly lower than the top surface of the Pico plate when fully snapped in place as seen in the picture below.

<img alt="Motor Controller In Place" src="../images/assembly/v3/MC_In_Plate3.jpg" width="500"/>


## Pico Install

Now take the Pico with the 4 connected wires and place beside the Pico plate to left of the motor controller.  At this time, do not place the Pico on the Pico plate, but just beside it so the wired side of the Pico is next to the motor controller so you can easily connect the wires to the motor controller.  Now connect the wires from the Pico to the motor controller as seen in the picture below with the GP10 and GP11 pins on the Pico connected to the INT 4 and INT 3 connections on the motor controller. Then connect the GP12 and GP13 pins of the Pico to the INT 2 and INT 1 of the motor controller.    

<img alt="Pico and Plate Parts" src="../images/assembly/v3/Pico_to_MC_Wire1.jpg" width="500"/>

<img alt="Pico and Plate Parts" src="../images/assembly/v3/Pico_to_MC_Wire2.jpg" width="500"/>

Turn the Pico so the pins are sticking up in the air and the USB jack is pointing away from you.  Now, place the Pico W on the raised pedestals on the plate.  These should align with the four holes in the Pico.

<img alt="Pico On Plate" src="../images/assembly/pico_on_plate_no_pegs.jpg" width="500"/>


Take your 4 plastic pegs and align them with the 4 holes on the Pico W. Do **NOT** push them all the way in yet.  Push the pins **halfway** down into the plate to secure it, but still leaving enough room raise the Pico a bit to route wires underneath it later.

<img alt="Pico On Plate With Pegs" src="../images/assembly/pico_plate_with_pegs.jpg" width="500"/>


## Motor Controller


***Motor Controller**  
<img alt="Motor Controller" src="../images/motor_controller.PNG" width="150"/>




- Pico plate
- Motor Controller
- 4 x plastic pegs


#### Wire the Motor Controller

Take your 5 10cm female to female wires and fish them under the Pico so that the female ends are on opposite sides of the Pico.

<img alt="Colored wires" src="../images/assembly/motor_controller_wires.jpg" width="500"/>

<img alt="Pico Motor Controller Wires Under 1" src="../images/assembly/motor_controller_wires_under1.jpg" width="500"/>

<img alt="Pico Motor Controller Wires Under 2" src="../images/assembly/motor_controller_wires_under2.jpg" width="500"/>

Connect the following pins using your blue, green, and yellow 4 x 10cm female to female wires.
These wires are actually in pairs. So, keep the yellow and blue wire pair next to each other on the motor controller and then Pico and then keep the blue and green pair of wires next to each other on the Pico and motor controller

| Motor controller pin | Pico pin |  Color |
|----------------------|----------|--------|
| INT1                 | GP13     | Green  |
| INT2                 | GP12     | Blue   |
| INT3                 | GP10     | Blue   |
| INT4                 | GP11     | Yellow |


**NOTE:** These pictures show the black wire connected at this point,  you'll do that in the next step.  
<img alt="Pico Motor Controller Wires topdown" src="../images/assembly/pico_plate_motor_controller_topdown.jpg" width="500"/>

<img alt="Pico Motor Controller Wires Ran Close up" src="../images/assembly/pico_plate_motor_controller_closeup.jpg" width="500"/>


Take the black or white 10cm female to female wire and connect it to the (-) negative terminal on the motor controller to a ground on the Pico.  We find the ground pin that is 3 down from the top right is best for this due to wire management.

<img alt="Pico Motor Controller Wires Ran" src="../images/assembly/pico_plate_motor_controller_topdown_arrow.jpg" width="500"/>  
<img alt="Pico Motor Controller Wires Ran" src="../images/assembly/pico_plate_motor_controller_closeup_usb.jpg" width="500"/>
At this point, the motor controller is just missing a cable to its (+) positive terminal and the 4 Motor pins on the bottom are unconnected.  We will connect those when we put the plate on the chassis.
Now, fully press down the 4 pegs that hold the Pico in place to secure it.  Don't use a ton of force and don't worry if they don't go all the way in.  They just need to keep the Pico from moving around or coming off the plate.

[next](https://github.com/javaplus/MadScientist/blob/main/lessons/assembly/chassis.md)
