# Head Assembly Instructions

## Parts List

Before beginning the assembly, ensure you have the following four printed parts and electronics ready:

* **Head Top:** 3D printed part with the top of the head and eyes already pre-assembled.
* **Chin Piece:** Includes two upward-facing tabs/slots.
* **Teeth & Gums:** 3D printed part featuring a laser slot and alignment slots.
* **LED Harness:** Pre-loaded with LEDs and wiring.
* **Laser Module**

![Jaw Components](images/assembly/head/chin_jaws.jpg)

---

## Assembly Steps

### 1. Electronics Preparation
If you haven't already, prepare the sub-assemblies:
* Insert the **Laser Module** into the center-front slot of the **Teeth & Gums** piece.
* Ensure the LEDs are loaded correctly into the **LED Harness**.

![Laser Insertion](images/assembly/head/teeth_lasers.jpg)
![Laser Front View](images/assembly/head/teeth_laser_front.jpg)
*Visual Check: Ensure the laser is seated flush in the front slot.*

### 2. Install the Chin
Take the **Chin Piece** and slide it up from underneath the **Teeth & Gums** piece.
* The chin should slide into the single long slot located at the far back of the gum piece.
* Ensure the two tabs from the chin piece protrude upward through the slot.

![Chin Installed](images/assembly/head/chin_with_teeth.jpg)
![Chin Side View](images/assembly/head/chin_with_teeth_side.jpg)
*Visual Check: Verify the chin fits snugly against the gums.*

### 3. Insert the LED Harness
* **Wire Management:** Move the laser wires to the side to ensure they do not obstruct the harness path.
* **Alignment:** Locate the long slot in the middle of the **LED Harness**. This slot must slide *between* the two tabs from the Chin piece (which are now sticking up through the gums).
* **Orientation:** Before inserting, confirm the wire order matches the harness assembly (red, black, green, blue) and orient the harness so the wires exit toward the rear of the head; the red wire should align with the left-most pin when viewing the head from the front (see `lessons/assembly/rgb.md` for detailed harness assembly and pin order).
* **Insertion:** Slide the LED harness down into the long slot.
* **Safety Check:** Verify that no wires are pinched during this process.

![Harness Insertion](images/assembly/head/INSERT_HARNESS_IMAGE_HERE.jpg)
*Visual needed: Top-down view showing the LED harness sliding between the chin tabs.*

### 4. Attach the Head Top
To finalize the head assembly:
1.  **Route Wires:** Position your wires out of the way to ensure a clean fit.
2.  **Front Alignment:** Locate the small lip under the nose of the **Head Top** piece. Catch this lip on the overhang located directly above the laser slot (between the front two teeth of the gum piece).
3.  **Rotate & Lock:** Once the nose is caught, rotate the bottom-back of the head down into the gums.
    * The head should line up with the two small slots on the gum piece.
4.  **Snap Fit:** Press down until you hear a satisfying snap, ensuring the assembly is secure.

![Head Attachment](images/assembly/head/INSERT_HEAD_ATTACH_IMAGE_HERE.jpg)
*Visual needed: Diagram showing the "Catch and Rotate" motion to attach the head.*

### 5. Final Wiring & Mounting
* **Connect the Laser and LED wires according to the Wiring Table below.** See `lessons/assembly/rgb.md` for harness assembly details.

**Wiring (canonical)**

- **LED Harness** (female ends to Pico):
  - RED  -> **GP22**
  - BLACK -> **GND**
  - GREEN -> **GP21**
  - BLUE -> **GP20**

- **Laser Module** (signal/pwm):
  - SIGNAL -> **GP16** (PWM)
  - GND -> **GND**
  - POWER -> **3.3V** or as specified by your laser module (check the module specs)
  - **Software note:** the laser is instantiated on pin 16 in `code/main.py` (e.g., `Laser(16)`).

> **Safety:** Do not point the laser at people, animals, or reflective surfaces. Use brief test pulses only.

**Testing the harness (recommended before final mounting)**

1. With the Pico powered and connected, run the simple LED blink example from `lessons/Led.md` (or `lessons/led_pwm.md` for PWM tests) to verify the LED harness colors/pins.
2. Use the `Laser` class from `code/laser.py` (for example, `laser.fire(1)`) to test the laser briefly — verify it turns on and is seated correctly.
3. Confirm no wires are pinched and that the harness sits flush in its slot.

* Slide the fully assembled head onto the rover body.