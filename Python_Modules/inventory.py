
''' Q17) Develop a Python script that opens an existing text file named "inventory.txt" in read mode and displays
the contents of the file line by line.'''

# Read from "inventory.txt"
try:
    with open("inventory.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("The file 'inventory.txt' does not exist.")