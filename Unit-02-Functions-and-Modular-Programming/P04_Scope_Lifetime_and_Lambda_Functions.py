
x = 10

def show():
    global x
    y = 5
    print("Local Variable:", y)
    x = x + 1
    print("Global Variable:", x)

show()

print("Global Outside Function:", x)

square = lambda n: n * n
cube = lambda n: n * n * n
maximum = lambda a, b: max(a, b)
addition = lambda a, b: a + b

print("Square:", square(4))
print("Cube:", cube(3))
print("Maximum:", maximum(10, 5))
print("Addition:", addition(5, 5))
