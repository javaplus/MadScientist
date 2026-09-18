# Power 

### Power Switch

### Parts
- 9 volt battery connector
- Power switch
- Power switch holder
- 10cm red female to female wire


<img alt="Power components" src="../images/assembly/v3/PowerSwitchParts.jpg" width="500"/>

Feed the red wire from the battery connector and one end from the 10cm red wire through the slot in the front of the chassis:

<img alt="Front Chassis Power Wire" src="../images/assembly/v3/PowerSwitchInstallChassis1.jpg" width="500"/>

Make sure the wire from the battery connector comes out from the inside of the chassis. The battery connector itself should be inside the chassis.

<img alt="Front Chassis Power Wire2" src="../images/assembly/v3/PowerSwitchInstallChassis2.jpg" width="500"/>

Get the power switch holder and feed the two red wires through the rectangular hole at the edge of the power switch.  

<img alt="Switch wires through switch holder" src="../images/assembly/v3/PowerSwitchInstallChassis3.jpg" width="500"/>


Connect one wire to the middle pin, and the other to either side.  The side that you connect the second or outer wire to will determine where the switch needs to be in order to be "on".

<img alt="Switch wires Installed" src="../images/assembly/v3/PowerSwitchInstall2.jpg" width="500"/>

The switch simply connects the two pins closest to it. For example, in the picture above, since the edge pin to the right is connected to the red wire, and the switch is pushed to the left, that means the switch is off.
Make a note of which direction is off and on.  Off will be when the switch is in the direction of the empty pin not connected to a wire. Put the switch in the OFF position now and try to leave it OFF until much later in the build when you are told to turn it ON.  
  
Now push the power switch and wires into the rectangular slot, pushing the red wires against the angled piece.  The red wires should make a sharp right angle inside the switch holder.  This helps hold the wires in place.  This can be a tight fit. See more instructions after picture if struggling.

<img alt="Switch in switch holder" src="../images/assembly/v3/PowerSwitchInstall3.jpg" width="500"/>

Fitting the power switch in the switch holder can be a very tight fit.  Borrow a pair of pliers or use two strong thumbs on each side of the black switch to push it into place.

<img alt="Switch in switch holder second view" src="../images/assembly/v3/PowerSwitchInstallChassis8.jpg" width="500"/>


<details >
<summary>Good Unit Test Opportunity</summary>
    After the power switch is securely in the power switch holder and connected to the 10cm red wire and the battery connector, this is a good time to test that your switch is working and making a continuous connection when on. Grab a lab instructor if available to help here. To do this, take a voltmeter or something similar to test continuity (Diode mode will work too).   The idea is to turn the switch to the on position and put the voltmeter leads on the positive battery connector and then the other end on the loose end of the 10cm wire to ensure that electricity can flow through the switch from the battery and out through the 10cm wire. 
</details>  

  
Now gently pull the red wires from inside the chassis to pull the switch holder assembly up against the outside of the chassis. The protruding side of the switch holder(where the wires are coming out) should fit into the slot on the chassis.

<img alt="Switch in chassis" src="../images/assembly/v3/PowerSwitchInstallChassis9.jpg" width="500"/>

### Battery Door Install  
### Parts
- Battery door
- Switch Key

<img alt="Battery Door" src="../images/assembly/v3/SwitchKeyAndDoorParts.jpg" width="500"/>

Put the battery door under the bottom center of the chassis with the raised square section up and towards the front (away from the hitch). 
The tabs on the battery door opposite the raised square go into the chassis first and act as a hinge point.  In the picture above, the tabs are on the right side.
Put the tabs up into the chassis and then pivot the raised square side up to be flush with the chassis.
While holding it there, take the switch key and guide the long "sword" like end under the switch holder already on the chassis.
The long narrow "sword" part should slide just under power switch holder through the same slot in the chassis that power switch holder is in.  This will lock it in place.

<img alt="Switch in chassis" src="../images/assembly/v3/SwitchKeyAndDoorChassis.jpg" width="500"/>

<img alt="Switch in chassis view 2" src="../images/assembly/v3/SwitchKeyAndDoorChassis1.jpg" width="500"/>  
<img alt="Switch in chassis view 3" src="../images/assembly/v3/SwitchKeyAndDoorChassis2.jpg" width="500"/>  

Continue to slide the battery key through until it holds the switch holder in place and the hex shape on the key fits into the similarly shaped hole on the switch holder.  

Battery door and key fully installed:  

<img alt="Switch fully installed" src="../images/assembly/v3/SwitchKeyAndDoorChassis3.jpg" width="500"/>

<img alt="Switch fully installed second view" src="../images/assembly/v3/SwitchKeyAndDoorChassis4.jpg" width="500"/>

<img alt="Switch fully installed third view" src="../images/assembly/v3/SwitchKeyAndDoorChassis5.jpg" width="500"/>

At this time, make sure the switch is turned off.  To turn off the power switch, push it in the direction of the single free pin not connected.

### Positive Power Connections
### Parts:
- 10cm Red Female to Female wire
- 10cm White Female to Female wire
- 10cm 3 way connector

<img alt="Voltage Regulator" src="../images/assembly/v3/PositivePowerParts.jpg" width="500"/>

The voltage regulator converts our 9 volt power source down to a steady 5 volts, which is what is required to operate the Pico.
The 3 pins from left to right are our input, ground, and output as seen in the picture above.

Grab your chassis with installed battery, battery switch, and motors.  Also, grab the voltage regulator and the red Y female to female cable.

<img alt="Chassis, Voltage Reg, Y wire" src="../images/assembly/power_regulator.jpg" width="500"/>

Connect the single end of the red Y wire to the far right of the voltage regulator.  This is the voltage output pin.  Push the female end up as far as you can, usually up to where the pin enlarges.
Be careful not to bend or break the pins on the voltage regulator.  If you do slightly bend the pins, it's not a big deal, just gently bend them back flat.  Constantly bending the pins can weaken them.

<img alt="Voltage Reg, Y wire" src="../images/assembly/power_regulator_positive_y.jpg" width="500"/>

Connect one of the black ground wires from the battery connector to the middle pin.

<img alt="Voltage Reg Ground" src="../images/assembly/power_regulator_negative_wire.jpg" width="500"/>

Connect the 10cm red wire that comes from the power switch to the far left pin on the regulator.

<img alt="Voltage Reg Input" src="../images/assembly/power_regulator_power_switch.jpg" width="500"/>

<img alt="Voltage Reg Input" src="../images/assembly/power_regulator_power_switch_2.jpg" width="500"/>

Carefully move the voltage regulator on top of the battery without disconnecting any of the wires.  The hole on top of the voltage regulator should go on one of the posts beside the battery.

<img alt="Voltage Reg In Chassis" src="../images/assembly/power_regulator_in_chassis.jpg" width="500"/>

[back](https://github.com/javaplus/MadScientist/blob/main/lessons/assembly/wheels.md)



[next](https://github.com/javaplus/MadScientist/blob/main/lessons/assembly/plate_chassis.md)
