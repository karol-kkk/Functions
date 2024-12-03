# main.py
from range_check import is_in_range

# Get the number and range from user input
number = int(input("A number: "))
x = int(input("Enter lower bound x: "))
y = int(input("Enter upper bound y: "))

if is_in_range(number, x, y):
    print(f"Number {number} in the range <{x},{y}>: yes")
else:
    print(f"Number {number} in the range <{x},{y}>: no")