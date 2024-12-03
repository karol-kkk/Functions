# mainmonth.py
from month_module import month

month_number = int(input("Enter month number: "))

month_name = month(month_number)

print(f"The name of month {month_number} is {month_name}")
