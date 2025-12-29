# LED Harness Assembly

## Parts Required

* **2x RGB LEDs (5mm):** These must be **Common Cathode** (where the long pin is Ground).
* **4x DuPont Wires (Female-to-Female or Female-to-Male):** Prepared to receive the LED pins.
* **Printed Harness Shell:** Two halves that snap together (part of the `head_parts` print).

![RGB and Harness Parts](../images/assembly/head/rgb_parts.jpg)
*Visual: The disassembled harness shell, LEDs, and wires.*

---

## Assembly Steps

### 1. Identify LED Pinout
Before connecting anything, identify the pins on your RGB LEDs.
* The **Longest Pin** is the **Common Ground (Cathode)**.
* When holding the LED so the pins point down and the flat side of the lens is to the left, the order is generally: **Red, Common (Ground), Green, Blue**.


> **Note:** We are using **Common Cathode** LEDs. If you wire this up and the colors are inverted or don't work, verify your LED type.

### 2. Add Wires to Clip
Take the male end of each wire and add them into the slotted portion of the clip as seen in the picture below. The tip of each male end should fit nicely in the slot at the top of the clip.  Make sure the slot order (left-to-right) is: **red, black (ground), green, blue**.

![Adding Wires](../images/assembly/head/rgb_wires_start.jpg)

![Adding Wires 2](../images/assembly/head/rgb_wires_end.jpg)

### 3. Add RGBs

Orient your RGB so that the longest pin is on the left (see picture above).  The longest pin should line up with the black wire, and the pin to the left of the longest pin should line up with the red wire.
When you have the LED in the right orientation, put its pins on top of the male end of the wires in the slots. You may have to spread the pins apart from each other just a bit so they can fit the pins in the slots.
Try to get as much of the pin into the slot as possible.  NOTE: In the picture below, the RGB Led to the right shows the correct orientation of the pins for both of the RGBs.

![Adding RGB](../images/assembly/head/rgb_wires_2.jpg)

After getting the first RGB in place, add the second on top of it.  Be sure its orientation is correct as well -- the longest pin from the RGB LED goes on top of the black wire's tip.  Again, you may have to spread the pins of the RGB LED apart a bit to line up with the slots.  You will also have to bend the pins a bit for both of them so that the top of each RGB so they don't get in the way. The easiest way to do this is hold all four pins firmly and slightly pull the LED top towards you.

![Adding RGB 2](../images/assembly/head/rgb_leds_installed.jpg)

### 4. Adding the Top Cover

Now with both RGB LEDs into the slotted clip, it's time to add the top cover.  Align the top cover so that the 4 lines will go directly over the RGB pins in the slots.  These lines go into the slots as well to ensure the RGB LED pins are held in place and contacting the male ends of the wires. Carefully snap the top cover on top of the bottom.

![Adding top](../images/assembly/head/rgb_cap_start.jpg)

![Adding top cover 2](../images/assembly/head/rgb_cap_start2.jpg)

Fully seat the top cover making sure its bottom part snaps around the bottom of the first piece.

![Fully Assembled](../images/assembly/head/rgb_final.jpg)

![Fully Assembled 2](../images/assembly/head/rgb_final2.jpg)

### 5. Connect the Wires (Harness)
We need to connect both LEDs to the same four wires (Parallel connection) so they light up in unison.

Make sure the slot order (left-to-right) matches: **red**, **black (ground)**, **green**, **blue**.

1.  **Group the Pins:** Align the two LEDs so their pins match (Red to Red, Ground to Ground, etc.).
2.  **Insert into Connectors:** Insert the corresponding pin pairs into the female ends of the DuPont wires.
    * All **Red** pins -> Red Wire
    * All **Ground** pins -> Black Wire
    * All **Green** pins -> Green Wire
    * All **Blue** pins -> Blue Wire
3.  *Tip:* Ensure the connection is snug. If using a specific connector housing (like in the image), push the pins in until they lock.

![Connecting Pins](../images/assembly/head/rgb1.jpg)
![Wires Connected](../images/assembly/head/rgb2.jpg)

### 6. Seat in the Harness
1.  **Align the Junctions:** Take the lower half of the 3D printed harness.
2.  **Place the Wires:** Lay the metal connection points (where the LED pins enter the DuPont connectors) into the four grooves inside the harness shell.
    * The plastic housing of the DuPont wire should sit just outside or flush with the internal stops.
    * The LED bulbs should be sticking out of the front.

![Seating the Wires](../images/assembly/head/rgb3.jpg)

### 7. Close the Assembly
1.  **Snap Shut:** Take the top half of the harness shell and press it down onto the bottom half.
2.  **Secure:** Squeeze firmly until the harness snaps shut, locking the wires in place.

![Closing the Harness](../images/assembly/head/rgb4.jpg)

### 8. Final Adjustment
1.  **Bend the LEDs:** Gently pull the two LEDs slightly apart and angle them outward.
2.  **Aim:** The goal is to angle them so that when the harness is inserted into the shark head, the lights shine directly into the eye sockets.

![Final Adjustment](../images/assembly/head/rgb5.jpg)
*Visual: The completed harness with LEDs angled for the eyes.*

---

## Wiring to Pico

Now connect the female end of the wires to the Pico.

**Wiring (canonical for the head harness):** RED -> **GP22**, BLACK -> **GND**, GREEN -> **GP21**, BLUE -> **GP20**. See the image below which is a zoomed in view of the [overall wiring diagram](../images/overall_layout.PNG).

> **Note:** These mappings are the canonical head wiring — see `lessons/assembly/head.md` for the head installation and final wiring table.

**Next Step:** Proceed to [Head Assembly](head.md) to install this harness into the rover.

