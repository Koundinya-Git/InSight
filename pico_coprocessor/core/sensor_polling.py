from drivers.hsr04 import HCSR04

# Initialize sensors using the GP pins from our wiring diagram
# Left Sensor: TRIG=GP14 (Pin 19), ECHO=GP15 (Pin 20)
sensor_left = HCSR04(trigger_pin=14, echo_pin=15)

# (You can easily add sensor_right, sensor_front, etc., here later using other GP pins)

def get_formatted_distances():
    """
    Reads the sensors and formats a string for the Pi 5.
    Example output: DIST:L,85.5
    """
    dist_l = sensor_left.distance_cm()
    
    # If out of range (-1.0) or absurdly far, cap it at 999 cm
    if dist_l < 0 or dist_l > 400: 
        dist_l = 999.0
    else:
        dist_l = round(dist_l, 1)
        
    return f"DIST:L,{dist_l}"