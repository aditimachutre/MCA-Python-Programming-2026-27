
def student_result(name, *marks, **info):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)

    print("Name:", name)
    print("Roll No:", info["roll"])

    return total, average, highest

t, a, h = student_result(
    "Amit", 80, 75, 90, roll=12
)

print("Total:", t)
print("Average:", a)
print("Highest:", h)
