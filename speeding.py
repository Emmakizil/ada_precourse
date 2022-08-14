"""
Write a function am_i_speeding that takes in a speed in units of kilometers per hour and a speed_limit in units of miles per hour. The function am_i_speeding should return

True if you are speeding
False if you are are not speeding
None if speed or speed_limit is not a float or an int.
The function am_i_speeding should use the following provided helper functions:

convert_km_to_mi to convert the speed to a mi/hr
validate_num to validate that speed and speed_limit are a float or an int
"""

def am_i_speeding(speed, speed_limit):
    if validate_num(speed) and validate_num(speed_limit):
        mySpead = convert_km_to_mi(speed)
        return mySpead > speed_limit
    return None

def convert_km_to_mi(num):
    return num*0.62137

def validate_num(num):
    if not isinstance(num, int) and not isinstance(num, float):
        return False
    else:
        return True

print(am_i_speeding(100, 55))