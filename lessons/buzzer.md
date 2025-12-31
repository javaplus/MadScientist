# Adding a Buzzer

Adding a buzzer to the Shark Rover allows it to communicate status updates, low battery warnings, or just play fun "disco" sounds.

## Parts Required

* **Passive Buzzer Module:** Ensure it is "Passive" (requires a PWM signal to generate tone), not "Active".
* **Jumper Wires:** Female-to-Female (or matching your header type).

## Wiring

Connect the buzzer to the Raspberry Pi Pico. We will use **GP15** for this example, located next to the Laser pin (GP16).

| Buzzer Pin | Pico Pin |
| :--- | :--- |
| **Signal / (+) / I/O** | **GP15** |
| **GND / (-) / Minus** | **GND** |
| **VCC** (If present) | **3.3V** |

> *Note: Simple 2-pin buzzers just need Signal and Ground. 3-pin modules may require VCC.*

---

## Technical Concept: How PWM Works

The Raspberry Pi Pico is a digital device, meaning it usually only sends "On" (3.3V) or "Off" (0V) signals. To make different sounds (or dim LEDs), we use **Pulse Width Modulation (PWM)**.

![PWM Duty Cycle Diagram](lessons/images/Pulse-Width-Modulation.jpg)  
*Figure: PWM creates an analog-like signal by switching on and off rapidly.*

PWM turns the digital pin on and off extremely fast—thousands of times per second. This creates a "square wave" that the buzzer vibrates to, creating sound.

### 1. Frequency = Pitch
**Frequency** is how many times per second the wave repeats (measured in Hertz, Hz).
* **Low Frequency (e.g., 100 Hz):** The buzzer diaphragm vibrates slowly, creating a deep, low sound.
* **High Frequency (e.g., 2000 Hz):** The diaphragm vibrates quickly, creating a high-pitched beep.

### 2. Duty Cycle = Volume (and Power)
**Duty Cycle** is the percentage of time the signal is "High" (On) versus "Low" (Off) during one cycle.
* In MicroPython, this is set using a 16-bit integer, where **0** is 0% and **65535** is 100%.
* For a buzzer, a **50% duty cycle** (around 32768) is typically the loudest, as the diaphragm pushes and pulls equally.

---

## Software Installation

### 1. The Buzzer Library
The buzzer class is already available in the repository.
* **File Location:** `code/buzzer.py`

Ensure this file is uploaded to your Pico. This class uses `asyncio` for non-blocking beeps (so the shark can keep driving while beeping) but also includes standard blocking functions for complex sound patterns.

### 2. Integration into Main
To use the buzzer in your main rover code (`main.py`):

1.  **Import:** Import the `Buzzer` class from the `buzzer` file.
2.  **Initialize:** Create a variable (e.g., `shark_sound`) and initialize the `Buzzer` on **pin 15**.
3.  **Usage:**
    * **Startup Sound:** Call `buzzDisco()` to play a sequence on startup (note: this may block execution for a few seconds).
    * **Status Beep:** Call `buzzTimeNFreq(time, frequency)` for non-blocking beeps while driving.
    * **Warning Tone:** Call `buzzLow()` for a continuous hum, and `stop()` to silence it.

## Troubleshooting
* **No Sound:** Check that you are connected to the correct GPIO pin and Ground.
* **Clicking/Static:** Ensure you are using a **Passive** buzzer. Active buzzers (which generate their own tone) do not work well with PWM signals.
* **Volume:** Passive buzzers driven directly by the Pico GPIO are generally quiet. Ensure the sticker is removed from the top of the buzzer.
