###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Enter a letter: ")
print("You entered:", letter)

number = int("20303")
print("Integer:", number)

binary = bin(304)
print("Binary representation:", binary)

hex = hex(304)
print("Hexadecimal representation:", hex)

unicode_code = ord('€')
print("Unicode code point:", unicode_code)

absolute = abs(-17)
print("Absolute value:", absolute)


import math

# Calculate the square root of 7
sqrt_7 = math.sqrt(7)
print("Square root of 7:", sqrt_7)

# Calculate the natural logarithm of 5 (ln(5))
ln_5 = math.log(5)
print("Natural logarithm of 5:", ln_5)

# Calculate the sine of 90 degrees (converted to radians)
sine_90 = math.sin(math.radians(90))
print("Sine of 90 degrees:", sine_90)


###
# Generates and prints a random number between 1 and 6,
# similar to rolling a dice
#
import random
dice_roll = random.randint(1, 6)
print("You rolled a:", dice_roll)


###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

area = triangle_area(a, b, c)
print("The area of the triangle is:", area)


# Calculates the sum of the digits in a number
def sum_digits(number):
    number = abs(number)
    number_str = str(number)
    total_sum = 0
    
    for digit in number_str:
        total_sum += int(digit) 
    
    return total_sum

any_number = int(input('Enter integer number: '))

result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')

###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    
    return grade

test_result = 15
final_grade = pts_to_grade(test_result)

print(f'You scored {test_result} points on the test. Your final grade is {final_grade}.')


###
# Function that returns the full name of a day of the week
# based on its number
#
def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number == 3:
        result = 'Wednesday'
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:
        result = 'Sunday'
    else:
        result = 'Invalid day number'
    
    return result

# Function usage
print('The name of day 5 in the week is', day_name(5))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))


###
# Converts letter to corresponding ICAO word
#
def icao(letter):
    letter = letter.capitalize()
    if letter == 'A':
        icao_name = 'Alfa'
    elif letter == 'B':
        icao_name = 'Bravo'
    elif letter == 'C':
        icao_name = 'Charlie'
    elif letter == 'D':
        icao_name = 'Delta'
    elif letter == 'E':
        icao_name = 'Echo'
    elif letter == 'F':
        icao_name = 'Foxtrot'
    elif letter == 'G':
        icao_name = 'Golf'
    elif letter == 'H':
        icao_name = 'Hotel'
    elif letter == 'I':
        icao_name = 'India'
    elif letter == 'J':
        icao_name = 'Juliett'
    elif letter == 'K':
        icao_name = 'Kilo'
    elif letter == 'L':
        icao_name = 'Lima'
    elif letter == 'M':
        icao_name = 'Mike'
    elif letter == 'N':
        icao_name = 'November'
    elif letter == 'O':
        icao_name = 'Oscar'
    elif letter == 'P':
        icao_name = 'Papa'
    elif letter == 'Q':
        icao_name = 'Quebec'
    elif letter == 'R':
        icao_name = 'Romeo'
    elif letter == 'S':
        icao_name = 'Sierra'
    elif letter == 'T':
        icao_name = 'Tango'
    elif letter == 'U':
        icao_name = 'Uniform'
    elif letter == 'V':
        icao_name = 'Victor'
    elif letter == 'W':
        icao_name = 'Whiskey'
    elif letter == 'X':
        icao_name = 'X-ray'
    elif letter == 'Y':
        icao_name = 'Yankee'
    elif letter == 'Z':
        icao_name = 'Zulu'
    else:
        icao_name = '???'

    return icao_name

# Function usage
name = input('Enter your name: ')
print('ICAO words for spelling out your name:')

for char in name:
    word = icao(char)
    print(word, end=" ") 



### Time format
   def time_string(hours, minutes, time_format):
    minutes_str = f"{minutes:02}"

    if time_format == '24':

        return f"{hours:02}:{minutes_str}"

    elif time_format == '12':
        period = "AM" if hours < 12 else "PM"
        hour_12 = hours % 12
        if hour_12 == 0:
            hour_12 = 12 
        return f"{hour_12}:{minutes_str} {period}"


print(time_string(12, 46, '12'))

