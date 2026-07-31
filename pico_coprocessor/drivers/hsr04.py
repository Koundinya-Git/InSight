import machine
import time

class HCSR04:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = machine.Pin(trigger_pin, machine.Pin.OUT)
        self.echo = machine.Pin(echo_pin, machine.Pin.IN)
        self.trigger.value(0)

    def distance_cm(self):
        self.trigger.value(0)
        time.sleep_us(5)
        self.trigger.value(1)
        time.sleep_us(10)
        self.trigger.value(0)

        signal_on = 0
        signal_off = 0
        
        timeout = time.ticks_us()
        while self.echo.value() == 0:
            signal_off = time.ticks_us()
            if time.ticks_diff(time.ticks_us(), timeout) > 30000: # 30ms timeout (~5 meters)
                return -1.0 # Out of range
                
        timeout = time.ticks_us()
        while self.echo.value() == 1:
            signal_on = time.ticks_us()
            if time.ticks_diff(time.ticks_us(), timeout) > 30000:
                return -1.0

        time_passed = time.ticks_diff(signal_on, signal_off)
        
        distance = (time_passed * 0.0343) / 2
        
        return distance