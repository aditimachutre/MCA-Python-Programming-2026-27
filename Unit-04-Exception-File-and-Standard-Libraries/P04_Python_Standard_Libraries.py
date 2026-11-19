
import math
import random
import datetime

# Math Library
num = 5.7

print("Square Root:", math.sqrt(25))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))
print("Ceiling:", math.ceil(num))
print("Floor:", math.floor(num))

# Random Library
numbers = [10, 20, 30, 40, 50]

print("Random Number:", random.randint(1, 100))
print("Random Element:", random.choice(numbers))

random.shuffle(numbers)
print("Shuffled List:", numbers)

# DateTime Library
today = datetime.date.today()

print("Current Date:", today)
print("Day:", today.day)
print("Month:", today.month)
print("Year:", today.year)

date1 = datetime.date(2026, 1, 1)
date2 = today

difference = date2 - date1

print("Date Difference:", difference.days, "days")
