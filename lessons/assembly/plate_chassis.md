# Add Plate on Chassis

### Parts
- Pico plate (with Pico and motor controller)
- Chassis

In this step, we will take the Pico plate with the Pico and motor controller and attach it to the chassis.  

Before we can put the plate down on the chassis, we need to connect the motors to the motor controllers pins that stick out below the plate.  Position the chassis so that the hitch is facing towards you.  The motor controller should be at the back of the chassis.
See below picture for proper orientation.   
Connect the front motor to the `motor A` pins on the motor controller.  The ``motor A`` pins are the first two pins on the left in the picture below.  Connect the rear motor to the `motor B` pins.  Run the wires for the rear motor over the battery.

<img alt="Pico Plate bottom view" height="500" src="/lessons/images/assembly/pico_plate_on_chassis_bottom.jpg"/>

Close up:

<img alt="Pico Plate bottom view closeup" src="/lessons/images/assembly/pico_plate_on_chassis_bottom_closeup.jpg" width="500"/>


Run the two ends of the red Y power cable from the voltage regulator up through the Pico plate and through the vertical slot to the right of the motor controller:

<img alt="Positive Power Cable Through Pico Plate" src="/lessons/images/assembly/pico_plate_bottom_power_cable.jpg" width="500"/>

Run the ground (black) wire from the battery connector up through the same vertical slot in the plate:

<img alt="Ground Cable Through Pico Plate" src="/lessons/images/assembly/pico_plate_bottom_power_cable_2.jpg" width="500"/>

Carefully push the plate down onto the chassis.  Make sure that the wires aren't disconnected or pinched between the plate and chassis.  The plate should sit flush with the cutout in the front and rear of the chassis.

<img alt="Pico Plate on Chassis" src="/lessons/images/assembly/pico_plate_on_chassis_power_cables.jpg" width="500"/>

Now it's time to connect the power cables from the voltage regulator and battery to the Pico and motor controller.

Take the two red wires and connect one to the Pico's VSYS pin (left side, second down from the top in the below picture).  The other red wire goes to the (+) pin on the motor controller.  

Here's a pinout diagram if you want to use it instead of the pictures:  
<details><summary> Click here to hide/show Pico Pin Out.</summary> 
 <img src="../images/picoPinOut.PNG"/>
</details>

The ground/black wire goes to a ground pin on the Pico.  We recommend the ground pin right next to the VSYS.  That is 3 pins down from the top left in the picture.

<img alt="Pico Plate on Chassis Power Connnected" src="/lessons/images/assembly/pico_plate_power_wire_routing_top.jpg" width="500"/>

<img alt="Pico Plate on Chassis USB Side" src="/lessons/images/assembly/pico_plate_usb_side.jpg" width="500"/>

<img alt="Pico Plate Front Installed" src="/lessons/images/assembly/pico_plate_installed_front.jpg" width="500"/>

Congratulations! You are super close to having a mobile rover!

[back](https://github.com/javaplus/MadScientist/blob/main/lessons/assembly/power.md)                


[next](https://github.com/javaplus/MadScientist/blob/main/lessons/assembly/tail.md)