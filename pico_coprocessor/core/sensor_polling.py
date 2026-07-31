from drivers.hsr04 import HCSR04

sensor_left = HCSR04(trigger_pin=14, echo_pin=15)


def get_formatted_distances():

    dist_l = sensor_left.distance_cm()
    
    if dist_l < 0 or dist_l > 400: 
        dist_l = 999.0
    else:
        dist_l = round(dist_l, 1)
        
    return f"DIST:L,{dist_l}"