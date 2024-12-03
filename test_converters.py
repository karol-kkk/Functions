import converters

print('### Test converters')

# Test m_to_cm function
print(f'Three meters is {converters.m_to_cm(3)} cm')

# Test cm_to_m function
print(f'532 cm is {converters.cm_to_m(532)} meters')

# Test cm_to_inch function
print(f'100 cm is {converters.cm_to_inch(100)} inches')

# Test feet_inch_to_cm function
print(f'6 feet 2 inches is {converters.feet_inch_to_cm(6, 2)} cm')
