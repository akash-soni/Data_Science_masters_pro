# employee_writer.py

import os

def write_employee_details(filename, employees):
    """
    Writes employee details to a text file in the current directory.
    
    Args:
    filename (str): The name of the file to write to.
    employees (list of dict): A list of dictionaries containing employee details.
    """
    current_directory = "16_ques"
    file_path = os.path.join(current_directory, filename)
    
    with open(file_path, 'w') as file:
        file.write("Name, Age, Salary\n")
        for employee in employees:
            file.write(f"{employee['name']}, {employee['age']}, {employee['salary']}\n")

if __name__ == "__main__":
    # List of employee details
    employees = [
        {"name": "Alice", "age": 28, "salary": 70000},
        {"name": "Bob", "age": 34, "salary": 85000},
        {"name": "Charlie", "age": 25, "salary": 50000},
        {"name": "David", "age": 45, "salary": 95000},
        {"name": "Eve", "age": 30, "salary": 60000}
    ]

    # Write employee details to the file
    write_employee_details("employees.txt", employees)

    print("Employee details have been written to employees.txt")
