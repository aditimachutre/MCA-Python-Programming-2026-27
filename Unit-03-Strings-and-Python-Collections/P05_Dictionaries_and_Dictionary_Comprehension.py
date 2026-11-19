
employee = {
    101: {"name": "Asha", "department": "IT", "salary": 40000},
    102: {"name": "Raj", "department": "HR", "salary": 30000}
}

# Add employee
employee[103] = {
    "name": "Neha",
    "department": "Sales",
    "salary": 45000
}

# Update salary
employee[101]["salary"] = 42000

# Display employee details
for emp_id, details in employee.items():
    print(emp_id, details)

# Search employee
search_id = int(input("Enter Employee ID: "))
print("Employee:", employee.get(search_id, "Not Found"))

# Dictionary comprehension
above_salary = {
    emp_id: details
    for emp_id, details in employee.items()
    if details["salary"] > 35000
}

print("Employees above 35000:", above_salary)

# Delete employee
del employee[102]

print("Updated Dictionary:", employee)
print("Keys:", employee.keys())
print("Values:", employee.values())
