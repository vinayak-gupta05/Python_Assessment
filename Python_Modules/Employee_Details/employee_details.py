
''' Q16) Write a Python program to create a text file named "employees.txt" and write the details of employees,
including their name, age, and salary, into the file.'''


# Employee details
employees = [
    {"name": "Alice", "age": 30, "salary": 70000},
    {"name": "Bob", "age": 28, "salary": 55000},
    {"name": "Charlie", "age": 35, "salary": 80000}
]

# Write to "employees.txt"
with open("employees.txt", "w") as file:
    for emp in employees:
        file.write(f"Name: {emp['name']}, Age: {emp['age']}, Salary: ${emp['salary']}\n")

print("Employee details written to 'employees.txt'")
