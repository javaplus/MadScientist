from machine import Pin
import time
from ir_rx.nec import NEC_8
from ir_tx.nec import NEC
import tm1637

# --- 1. HARWARE SETUP ---
# Display
display = tm1637.TM1637(clk=Pin(14), dio=Pin(13))
display.brightness(7) 
display.show("0000") 

# Indicator (Buzzer/LED)
indicator = Pin(15, Pin.OUT, value=0)

# IR Transmitter Setup (New)
tx_pin = Pin(17, Pin.OUT, value=0)
transmitter = NEC(tx_pin)
HARNESS_ID = 99  # The unique ID of the test harness

# --- 2. HIT DETECTION LOGIC ---
hit_flag = False
current_shark_id = 0

def hit_detected(data, addr, ctrl):
    global hit_flag, current_shark_id
    
    # Ignore our own shots bouncing back into the receiver
    if addr == HARNESS_ID:
        return 
        
    current_shark_id = addr
    hit_flag = True
    print(f"Hit by Shark {addr}!")

# IR Receiver Setup
rx_pin = Pin(16, Pin.IN)
ir_receiver = NEC_8(rx_pin, hit_detected)

print(f"Harness Ready. Shooting as ID {HARNESS_ID} and listening...")

# --- 3. NON-BLOCKING MAIN LOOP ---
# Set up our "stopwatches"
last_shot_time = time.ticks_ms()
display_clear_time = 0

while True:
    current_time = time.ticks_ms()
    
    # TASK A: Shoot an IR burst every 1.5 seconds (1500 milliseconds)
    if time.ticks_diff(current_time, last_shot_time) > 1500:
        transmitter.transmit(HARNESS_ID, 100) # Send Harness ID (99) and a generic command (100)
        last_shot_time = current_time # Reset the shooting stopwatch

    # TASK B: Handle an incoming hit from a Shark
    if hit_flag:
        indicator.value(1)
        display.show('{:04d}'.format(current_shark_id))
        
        # Set a stopwatch to clear the display 5000ms (5s) in the future
        display_clear_time = time.ticks_add(current_time, 5000) 
        hit_flag = False

    # TASK C: Check if 5 seconds have passed since the last hit
    # If the timer is active (>0) AND the current time has passed the target clear time
    if display_clear_time > 0 and time.ticks_diff(current_time, display_clear_time) > 0:
        indicator.value(0)
        display.show("0000")
        display_clear_time = 0 # Turn off the clear timer
        
    # A tiny sleep keeps the loop running efficiently without maxing out the CPU
    time.sleep(0.02)
