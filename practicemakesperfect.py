# Function to check if the string is a valid binary number
def f(binary_number):
    return all(char in '01' for char in binary_number)

def main():
    print(f'"101101" is valid binary? {f("101101")}')
    print(f'"1311a10100" is valid binary? {f("1311a10100")}')

# This block will only execute when the script is run directly
if __name__ == "__main__":
    main()

#### Vending machine
def f(amount_to_pay):
    coins = amount_to_pay // 5
    amount_to_pay %= 5

    coins += amount_to_pay // 2
    amount_to_pay %= 2

    coins += amount_to_pay

    return coins

# Main function
def main():
    amount = int(input("Enter the amount to pay: "))
    print(f"Minimum number of coins needed: {f(amount)}")

if __name__ == "__main__":
    main()


#### The sum of the digits of a number

# Function to compute the sum of even or odd digits
def f(number, even):
    # Initialize the sum
    digit_sum = 0

    # Loop through each digit in the number
    for digit in str(number):
        digit = int(digit)
        if even and digit % 2 == 0:
            digit_sum += digit  # Add even digits
        elif not even and digit % 2 != 0:
            digit_sum += digit  # Add odd digits

    return digit_sum

# Main function
def main():
    # Test cases
    print(f"Sum of even digits in 3124: {f(3124, True)}")  # Expected: 6
    print(f"Sum of odd digits in 3124: {f(3124, False)}")  # Expected: 4
    print(f"Sum of odd digits in 20576: {f(20576, False)}")  # Expected: 12
    print(f"Sum of even digits in 20576: {f(20576, True)}")  # Expected: 8
    print(f"Sum of even digits in 13115: {f(13115, True)}")  # Expected: 0

# This block will only execute when the script is run directly
if __name__ == "__main__":
    main()


# Function to compute the sum of even or odd digits
def f(number, even):
    digit_sum = 0

    for digit in str(number):
        digit = int(digit)
        if even and digit % 2 == 0:
            digit_sum += digit  
        elif not even and digit % 2 != 0:
            digit_sum += digit 

    return digit_sum

# Main function
def main():
    print(f"Sum of even digits in 3124: {f(3124, True)}")  
    print(f"Sum of odd digits in 3124: {f(3124, False)}")  
    print(f"Sum of odd digits in 20576: {f(20576, False)}")  
    print(f"Sum of even digits in 20576: {f(20576, True)}")  
    print(f"Sum of even digits in 13115: {f(13115, True)}")  

if __name__ == "__main__":
    main()


# Function to count the number of negative even numbers in the range <x, y>
def f(x, y):
    negative_even_count = 0
    
    for num in range(x, y + 1):
        if num < 0 and num % 2 == 0:
            negative_even_count += 1
    
    return negative_even_count

# Main function
def main():
    print(f"Number of negative even numbers between -7 and 8: {f(-7, 8)}")  
    print(f"Number of negative even numbers between -1 and 11: {f(-1, 11)}")  

if __name__ == "__main__":
    main()


# Function to check if at least one number is negative
def f(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0

# Main function
def main():
    print(f"f(11, 6, -4) returns: {f(11, 6, -4)}")  
    print(f"f(5, 4, 14) returns: {f(5, 4, 14)}")    

if __name__ == "__main__":
    main()


# Function to return a string of n asterisks separated by slashes
def f(n):
    return '/'.join(['*'] * n)

# Main function
def main():
    print(f"f(4) returns: {f(4)}") 
    print(f"f(1) returns: {f(1)}") 

if __name__ == "__main__":
    main()


# Function to return numbers from 1 to n as a string
def f(n):
    return ''.join(str(i) for i in range(1, n + 1))

# Main function
def main():
    print(f"f(11) returns: {f(11)}") 
    print(f"f(4) returns: {f(4)}")    


if __name__ == "__main__":
    main()


# Function to perform the arithmetic operation based on the operator
def f(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    else:
        return "Invalid operator"

# Main function
def main():

    print(f"f(2, 3, '+') returns: {f(2, 3, '+')}")  
    print(f"f(2, 3, '%') returns: {f(2, 3, '%')}")  
    print(f"f(2, 3, '**') returns: {f(2, 3, '**')}")  
    print(f"f(2, 3, '*') returns: {f(2, 3, '*')}")
    print(f"f(2, 3, '-') returns: {f(2, 3, '-')}")  

if __name__ == "__main__":
    main()

#### People in the room counter
def f(detector):
    count = 0 
    for action in detector:
        if action == "+":
            count += 1  # A person enters
        elif action == "-":
            count -= 1  # A person leaves
            
        if count >= 3:
            return True
    
    return False

# Main function to test
def main():
    print(f'f("+-+++-+---") returns: {f("+-+++-+---")}')  
    print(f'f("+-+-+-+-") returns: {f("+-+-+-+-")}') 
    print(f'f("+-++-+--") returns: {f("+-++-+--")}')  
    print(f'f("+-++-++-+---") returns: {f("+-++-++-+---")}')  

if __name__ == "__main__":
    main()

    #### Fibonacci
def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1  # First two Fibonacci numbers
        for _ in range(3, n + 1):
            a, b = b, a + b 
        return b

# Main function to test
def main():
    print(f"f(5) returns: {f(5)}") 
    print(f"f(9) returns: {f(9)}") 

if __name__ == "__main__":
    main()


#### Palindrome
def f(palindrome):
    cleaned = ''.join(c for c in palindrome if c.isalnum()).lower()
    
    return cleaned == cleaned[::-1]

def main():
    print(f("radar"))  
    print(f("12-11-21"))  
    print(f("book"))  

if __name__ == "__main__":
    main()

#### Sentence space remover
def f(sentence):
    return sentence.replace(" ", "")

def main():
    sentence1 = "integrated development environment"
    sentence2 = "A programming language is a system of notation for writing computer programs"
    
    print(f(sentence1))  
    print(f(sentence2)) 

if __name__ == "__main__":
    main()

#### Sum of repeated digits
def f(number):
    num_str = str(number)

    digit_count = {}
    
    for digit in num_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    repeated_sum = 0
    for digit, count in digit_count.items():
        if count > 1:
            repeated_sum += int(digit) * (count - 1)  
    
    return repeated_sum

def main():

    print(f(1027))      
    print(f(230335))     
    print(f(513553007))   

if __name__ == "__main__":
    main()


#### Prime number
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def f(n):
    count = 0  
    number = 2  
    
    while count < n:
        if is_prime(number):
            count += 1
        number += 1
    
    return number - 1  

def main():
    print(f(1))  
    print(f(5))  

if __name__ == "__main__":
    main()

#### The difference between the largest and smallest numbers.
def f(number1, number2, number3):
    largest = max(number1, number2, number3)  
    smallest = min(number1, number2, number3) 
    return largest - smallest 

def main():
    print(f(7, 4, 9)) 
    print(f(2, 12, 8))  

if __name__ == "__main__":
    main()

#### Acronym
def f(name):
    words = name.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

def main():
    print(f("Internet of Things"))  
    print(f("For Your Information"))  
    print(f("Python"))  

if __name__ == "__main__":
    main()

#### Password
def f(password):
    if len(password) < 6:
        return False
    
    if len(set(password)) != len(password):
        return False
    
    return True

def main():
    print(f("ax15")) 
    print(f("book123"))  
    print(f("A2water3")) 
    print(f("qwerty"))  
    print(f(""))

if __name__ == "__main__":
    main()

#### Adding and subtracting
def f(expression):

    return eval(expression)

def main():

    print(f("2+3"))      
    print(f("3+8+1"))      
    print(f("2+3-4+5-0"))  

if __name__ == "__main__":
    main()

####  sum of numbers in the range <x,y> that are completely divisible by 2 and 3 and not divisible by 4
def f(x, y):
    total_sum = 0
    for number in range(x, y + 1): 
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total_sum += number
    return total_sum

def main():
    print(f(1, 20))  
    print(f(10, 30))  

if __name__ == "__main__":
    main()

#### Text with dash
def f(text):
    return '-'.join(text)

def main():
    print(f("Univesity"))  
    print(f("UE"))         
    print(f("x"))         
    print(f(""))     

if __name__ == "__main__":
    main()

### Product code validator
def f(product_code):

    digits = [int(digit) for digit in product_code]
    sum_of_digits = sum(digits[:3])
    control_digit = sum_of_digits % 7
    
    return control_digit == digits[3]

def main():
    print(f("1082"))  
    print(f("2035"))  
    print(f("1114"))  
    print(f("7071"))  

if __name__ == "__main__":
    main()


#### Dice
def f(dice):
    max_count = 1 
    current_count = 1 

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:  
            current_count += 1  
        else:
            max_count = max(max_count, current_count)  
            current_count = 1 

    max_count = max(max_count, current_count)

    return max_count

def main():
    print(f("5233165554211")) 
    print(f("2133"))           
    print(f("1111"))           
    print(f("12456"))        

if __name__ == "__main__":
    main()

#### Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    if n > 1:
        return n * factorial(n - 1)

n = 5
result = factorial(n)
print(f"The factorial of {n} is: {result}")

### Sum of natural numbers
def sum_natural(n):
    if n == 1:
        return 1
    
    return n + sum_natural(n - 1)

n = 10
result = sum_natural(n)
print(f"The sum of natural numbers from 1 to {n} is: {result}")

#### Power of xn
def power(x, n):
    if n == 0:
        return 1
    
    return x * power(x, n - 1)

x = 5
n = 3
result = power(x, n)
print(f"{x}^{n} = {result}")
