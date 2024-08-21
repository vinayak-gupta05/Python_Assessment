
''' Q18) Create a Python script that reads a text file named "expenses.txt" and calculates the total amount spent
on various expenses listed in the file.'''

# Calculate total expenses from "expenses.txt"
total_expenses = 0

try:
    with open("expenses.txt", "r") as file:
        for line in file:
            try:
                amount = float(line.strip())
                total_expenses += amount
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
except FileNotFoundError:
    print("The file 'expenses.txt' does not exist.")

print(f"Total expenses: ${total_expenses:.2f}")