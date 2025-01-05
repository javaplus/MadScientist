# Attaching the Tail

### Parts
- Tail with Tail Tip and Photoresistor installed
- Plastic power switch
- Tail connector

![Tail and Power Switch Parts](/lessons/images/assembly/tail_power_parts.jpg)


### Add Power Switch

Take the 3D Printed power switch and notice there are 3 small notches or slots in the bottom of it as seen in the picture below.

![Power Switch Notches](/lessons/images/assembly/power_switch.jpg)  

Make sure the physical power switch which you wired earlier is in the fully down position before adding the 3D printed power switch ontop of it.
Hold your power switch in the orientation as seen in the picture above so you can see the slots and then place it over the physical power switch on the back of the chassis.
Make sure to put the power switch into the top most slot/notch of the 3D printed power switch.  It's easier to do this if you tip the back of the Rover up.

![Power Switch on Chassis](/lessons/images/assembly/power_switch_1.jpg)  

Zoomed View of Switch:
![Power Switch on Chassis](/lessons/images/assembly/power_switch_on_chassis.jpg)


### Tail Connector

Now take the tail connector piece and slide the square frame over the power box that contains the power switch.  Note that the 3 slots go up towards the top and the first two slots should go over the chassis.  The thinner vertical part of the frame goes in the vertical slot of the power switch.  See the pictures below for correct orientation and installation.

![Tail Connector](/lessons/images/assembly/tail_connector1.jpg)

![Tail Connector 2](/lessons/images/assembly/tail_connector2.jpg)

![Tail Connector 3](/lessons/images/assembly/tail_connector_3.jpg)


Hold the tail connector you just installed in place and see if you can actuate the power switch up and down.  It should slide relatively easily with just a little resistance.  Be careful not to use too much force.


### Connect the tail

Now the tail can be slid into the slots of the tail connector.  The leading slot of the tail goes into the leading slot of the tail connector.  

![Tail Attaching](/lessons/images/assembly/tail_attaching1.jpg)

![Tail Connected](/lessons/images/assembly/tail_attached1.jpg)

![Tail Connected](/lessons/images/assembly/tail_attached2.jpg)

Once tail is slid correctly into the tail connector slots, the tail should lock the tail connector to the chassis and hold the extended power switch in place.


### Wire the Tail

Now we are going to connect the photoresistor in the tail to the Pico.  If you have a lot of excess wire sticking out of the tail, you may want to loop them into a really loose knot.

![Tail Wires](/lessons/images/assembly/tail_wires_circle.jpg)

Connect the red wire to the `3V3` pin on the Pico which is 4 pins down from the `VSYS` power pin the voltage regulator is connected to.
Connect the blue or yellow wire from the photoresistor to the `GP28_A2` pin which is 2 pins below the `3V3` pin.

Now we simply connect the black wire to a GND pin on the Pico.  We are using the AGND pin on the Pico which is directly below the `GP28_A2` pin. 

NOTE: The 3 photoresistor wires are marked with yellow lines in the pictures below:

![Tail Wires connected](/lessons/images/assembly/tail_wires_attached.jpg)

![Tail Wires connected](/lessons/images/assembly/tail_wires_attached_close.jpg)


Your tail is now attached and ready for some swimming!