import machine
import time
import math
import uasyncio as asyncio

class MicroServo:
    def __init__(self, pin: int, min_angle: int = 0, max_angle: int = 180, min_pulse: int = 500, max_pulse: int = 2500):
        self.pin = machine.Pin(pin, machine.Pin.OUT)
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.angle = 0

    def set_angle(self, angle: int):
        if angle < self.min_angle or angle > self.max_angle:
            raise ValueError(f"Angle must be between {self.min_angle} and {self.max_angle}")
        
        pulse_width = int(self.min_pulse + (angle - self.min_angle) * (self.max_pulse - self.min_pulse) / (self.max_angle - self.min_angle))
        self.pin.duty(pulse_width)
        self.angle = angle

    async def sweep(self, start_angle: int, end_angle: int, step: int, delay: float):
        for angle in range(start_angle, end_angle + step, step):
            self.set_angle(angle)
            await asyncio.sleep(delay)