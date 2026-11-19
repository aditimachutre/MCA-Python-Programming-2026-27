
def add(a, b=0):
    return a + b

def sub(a, b=0):
    return a - b

def mul(a, b=1):
    return a * b

def div(a, b=1):
    return a / b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", add(x, y))
print("Subtraction:", sub(a=x, b=y))
print("Multiplication:", mul(x, y))
print("Division:", div(x, y))
