data = float(input("Enter data usage in GB: "))

if data <= 1:
    bill = 50

elif data <= 5:
    bill = 50 + (data - 1) * 20

elif data <= 10:
    bill = 130 + (data - 5) * 15

else:
    bill = 205 + (data - 10) * 10

print("Mobile Data Bill =", bill)