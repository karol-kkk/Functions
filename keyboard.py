# Functions to read any data type from the keyboard

def input_string(message):
    return input(message)  

def input_integer(message):
    return int(input(message)) 

def input_real(message):
    return float(input(message)) 

def input_boolean(message):
    value = input(message).lower()  
    if value == 'y':
        return True
    elif value == 'n':
        return False