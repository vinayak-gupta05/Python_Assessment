
# 15) Write a Python module named file_operations.py with functions for reading, writing, and appending data to a file.


def read_file(file_path):
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."


def write_file(file_path, data):
    
    with open(file_path, 'w') as file:
        file.write(data)


def append_to_file(file_path, data):
    
    with open(file_path, 'a') as file:
        file.write(data)