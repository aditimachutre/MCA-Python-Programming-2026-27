age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
credit = int(input("Enter credit score: "))

if age >= 21 and age <= 60 and income >= 25000 and credit >= 700:
    print("Person is Eligible for Loan")
else:
    print("Person is Not Eligible for Loan")