
# Write student details
f = open("student.txt", "w")
f.write("Name: Riya, Roll No: 10\n")
f.close()

# Append student details
f = open("student.txt", "a")
f.write("Name: Amit, Roll No: 11\n")
f.close()

# Read complete file
f = open("student.txt", "r")
print(f.read())
f.close()

# Read file line by line
f = open("student.txt", "r")

for line in f:
    print(line.strip())

f.close()
