
name = input("Enter full name: ")
email = input("Enter email: ")
mobile = input("Enter mobile number: ")

space = name.find(" ")

first = name[:space]
last = name[space + 1:]

print("First Name:", first)
print("Last Name:", last)
print("Reverse Name:", name[::-1])

username, domain = email.split("@")

print("Username:", username)
print("Domain:", domain)

print("Last 4 Digits:", mobile[-4:])

print("First Character:", name[0])
print("Last Character:", name[-1])

print(f"Student Name: {name}")
print("Email: {}".format(email))
print("Mobile: {}".format(mobile))
