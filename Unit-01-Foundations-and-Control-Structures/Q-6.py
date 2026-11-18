percentage = float(input("Enter percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid Percentage")

elif percentage >= 90:
    print("Grade A")

elif percentage >= 75:
    print("Grade B")

elif percentage >= 60:
    print("Grade C")

elif percentage >= 50:
    print("Grade D")

elif percentage >= 35:
    print("Grade E")

else:
    print("Grade F - Fail")