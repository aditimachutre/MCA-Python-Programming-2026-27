
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Division:", a / b)

    numbers = [10, 20, 30]
    index = int(input("Enter list index: "))
    print("List Value:", numbers[index])

    age = int(input("Enter age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above")

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError as e:
    print("Invalid Value:", e)

except IndexError:
    print("Invalid list index")

else:
    print("No Exception Occurred")

finally:
    print("Program Completed")
