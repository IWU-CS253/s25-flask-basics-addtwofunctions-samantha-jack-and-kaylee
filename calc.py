# calc.py
import math

def calculate(current_value, num, clear):
    if clear:
        return ''  # Clear the current value if clear button is pressed
    elif num:
        if num == '=':
            # Calculate result if '=' is pressed
            try:
                # Safely evaluate the current expression
                return str(eval(current_value))
            except:
                return 'Error'
        elif num == "^2":
            current_value = int(current_value) * int(current_value)
        elif num == "√":
            current_value = math.sqrt(float(current_value))
        else:
            # Append the pressed button value to the current value
            return current_value + num
    return current_value
