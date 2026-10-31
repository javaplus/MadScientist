from machine import Pin
import asyncio
import utime
from ir_tx import NEC


class IRLaser:
    """IR LED transmitter using the NEC protocol.

    Replaces the PWM laser with an IR LED.  Every transmission carries
    this rover's shark_id as both the NEC address and data fields, which
    encodes the shark identity on the wire.

    Methods mirror the original Laser class so game modes work unchanged:
        fire(seconds)  – repeatedly transmit for the given duration
        turnOn()       – arm the laser; begins a slow heartbeat transmission
        turnOff()      – disarm; stops all transmission
        stop()         – alias for turnOff()
    """

    # Time between NEC bursts while actively firing (~NEC repeat rate)
    FIRE_INTERVAL = 0.11
    # Time between NEC bursts during heartbeat (armed/idle state)
    HEARTBEAT_INTERVAL = 0.5

    def __init__(self, pin_number, rover_name, shark_id):
        self.ir = NEC(Pin(pin_number, Pin.OUT))
        self.rover_name = rover_name
        # NEC address and data are each 8 bits
        self.shark_id = shark_id & 0xFF
        self._active_task = None

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def fire(self, seconds):
        """Transmit repeatedly for *seconds* duration."""
        self._cancel_active_task()
        self._active_task = asyncio.create_task(self._fire_task(seconds))

    def turnOn(self):
        """Arm: begin slow heartbeat transmissions until turnOff() is called."""
        self._cancel_active_task()
        self._active_task = asyncio.create_task(self._heartbeat_task())

    def turnOff(self):
        self.stop()

    def stop(self):
        """Stop all active IR transmissions."""
        self._cancel_active_task()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _transmit(self):
        # addr = shark_id  →  identifies this rover
        # data = shark_id  →  additional payload (shark name, encoded as ID)
        self.ir.transmit(self.shark_id, self.shark_id)

    def _cancel_active_task(self):
        if self._active_task is not None:
            self._active_task.cancel()
            self._active_task = None

    async def _fire_task(self, seconds):
        deadline = utime.ticks_add(utime.ticks_ms(), int(seconds * 1000))
        while utime.ticks_diff(deadline, utime.ticks_ms()) > 0:
            self._transmit()
            await asyncio.sleep(self.FIRE_INTERVAL)
        self._active_task = None

    async def _heartbeat_task(self):
        while True:
            self._transmit()
            await asyncio.sleep(self.HEARTBEAT_INTERVAL)
