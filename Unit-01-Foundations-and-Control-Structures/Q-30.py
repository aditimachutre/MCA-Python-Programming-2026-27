n = int(input("Enter number of students: "))

marks = []

for i in range(n):

    mark = float(input("Enter marks of student " + str(i + 1) + ": "))

    marks.append(mark)

total = sum(marks)
average = total / n

highest = max(marks)
lowest = min(marks)

passed = 0
failed = 0
above75 = 0

for mark in marks:

    if mark >= 35:
        passed = passed + 1
    else:
        failed = failed + 1

    if mark > 75:
        above75 = above75 + 1

print("\n----- CLASS RESULT -----")
print("Class Average =", average)
print("Highest Marks =", highest)
print("Lowest Marks =", lowest)
print("Passed Students =", passed)
print("Failed Students =", failed)
print("Students Scoring Above 75% =", above75)