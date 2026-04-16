# 🧪 Mad Scientist — Event Build Notes

This guide is designed to help you get your kit running quickly and safely. Because these kits are shared and reused, the most important rule is: **Build smart, not permanent.**

---

## 🛑 The Golden Rules (Read This First!)
To ensure these kits work for the next person, follow these rules strictly:
* **No Permanent Changes:** Never cut wires, solder, glue, drill, or sand any parts. 
* **Hands Off the Repairs:** If a part looks broken, frayed, or won't fit, **stop and ask a facilitator.** Do not attempt your own repairs.
* **The "Reversible" Rule:** If you can’t undo what you just did in 10 seconds, you’re doing it wrong.

---

## 🔍 Step 1: The Visual Audit
Before building, see how much is already done. **If the head looks complete (eyes, teeth, and laser are in), do not open it.**

**Check your kit for these pre-assembled parts:**
* [ ] **The Head:** Are eyes, teeth, and laser already installed?
* [ ] **The Plate:** Is the Pico and Motor Controller already attached?
* [ ] **Wiring:** Are there already wire harnesses plugged in?

---

## ⚡ Step 2: Choose Your Build Path
Follow the path that matches your kit’s current state.

### Path A: The "Fast Path" (Mostly Assembled)
*Use this if your head and chassis are already mostly put together.*
1.  **Wiring:** Open the [Overall Wiring Diagram](lessons/images/overall_layout.PNG). This is your **Source of Truth**. Connect only the remaining loose wires.
2.  **Firmware:** Flash or verify the code using the [Firmware Guide](lessons/firmware.md).
3.  **Bench Test:** Power on and test the LEDs and motors *before* you snap the head onto the body.

### Path B: The "Full Build" (Missing Parts)
*Only follow these specific guides for the parts missing from your kit:*
1.  **Brain & Power:** [Pico/Motor Plate](lessons/assembly/plate.md) → [Chassis Integration](lessons/assembly/plate_chassis.md) → [Power System](lessons/assembly/power.md).
2.  **Movement:** [Motors](lessons/assembly/chassis.md) → [Wheels & Tracks](lessons/assembly/wheels.md).
3.  **Sensors & Style:** [Head/LEDs](lessons/assembly/head.md) → [RGB Setup](lessons/assembly/rgb.md) → [Tail](lessons/assembly/tail.md).

---

## 🔌 Wiring & Connections
The wiring diagram is the final authority. If a tutorial says one thing but the diagram says another, **follow the diagram.**

* **Wiring Diagram:** [View Layout Image](lessons/images/overall_layout.PNG)
* **Pin Reference:** See the "Wiring Reference" in the [README.md](README.md#-wiring-reference).
* **Pro Tip:** If a connector doesn't slide in easily, check the alignment. **Never force a plug.**

---

## 🛠 Troubleshooting (Quick Fixes)

| Issue | Check This First |
| :--- | :--- |
| **No Power** | Check battery orientation and the physical power switch. |
| **Motor Swapped** | If the bot moves backward, ask a facilitator to run a "Motor Direction Test." |
| **Wrong LED Colors** | Your RGB harness might be upside down. Check the [RGB Guide](lessons/assembly/rgb.md). |
| **Smoke or Smell** | **Switch off power immediately** and notify a facilitator. |

---

## 🚀 Final Assembly
Once your electronics are tested and working:
1.  **Mount the Head:** Align the head unit with the chassis. It should slide or snap into place without force.
2.  **Secure the Cap:** Install the final top piece (the "Cap"). If unsure which piece this is, ask a facilitator.
3.  **Safety Check:** Ensure no wires are pinched or dragging on the wheels.

---

## 📚 Essential Links
* [Master Wiring Diagram](lessons/images/overall_layout.PNG)
* [Firmware & Code Install](lessons/assembly/code_install.md)
* [Full Parts List](resources/PartsList.md)

> **⚠️ LASER SAFETY:** This kit contains a Laser. Never look directly into the beam or point it at anyone’s eyes. (Facilitator will confirm safety protocol before use).