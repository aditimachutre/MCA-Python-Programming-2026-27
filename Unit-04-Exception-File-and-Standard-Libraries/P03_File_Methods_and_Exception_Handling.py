
try:
    f = open("student.txt", "r")

    print("File Name:", f.name)
    print("File Mode:", f.mode)

    print("Reading File:")
    print(f.read())

    print("File Position:", f.tell())

    f.seek(0)
    print("First Line:", f.readline())

    f.seek(0)
    print("All Lines:", f.readlines())

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")

else:
    print("File read successfully")

finally:
    try:
        f.close()
    except NameError:
        pass
