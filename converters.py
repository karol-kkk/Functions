def m_to_cm(n):
    return n * 100

def cm_to_m(n):
    return n / 100

def cm_to_inch(n):
    return n / 2.54

def feet_inch_to_cm(feet, inches):
    return feet * 30.48 + inches * 2.54

if __name__ == "__main__":
    # Only execute when you run this module, so you can test the functions here
    print(f'2 meters = {m_to_cm(2)} cm')
    print(f'532 cm = {cm_to_m(532)} meters')
    print(f'100 cm = {cm_to_inch(100)} inches')
    print(f'5 feet 10 inches = {feet_inch_to_cm(5, 10)} cm')
