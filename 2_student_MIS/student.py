"""
2. Design and implement a Python program for managing student information using object-oriented principles. Create a class called `Student` with encapsulated attributes for name, age, and roll number.
Implement getter and setter methods for these attributes. Additionally, provide methods to display student information and update student details.

Tasks

- Define the `Student` class with encapsulated attributes
- Implement getter and setter methods for the attributes
- Write methods to display student information and update details
- Create instances of the `Student` class and test the implemented functionality.

"""

class Student:
    def __init__(self, name, age, roll_number):
        self.__name = name
        self.__age = age
        self.__roll_number = roll_number

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_roll_number(self):
        return self.__roll_number

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age! Age must be positive.")

    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    # Method to display student information
    def display_info(self):
        print(f"Student Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Roll Number: {self.__roll_number}")

    # Method to update student details
    def update_details(self, name=None, age=None, roll_number=None):
        if name is not None:
            self.set_name(name)
        if age is not None:
            self.set_age(age)
        if roll_number is not None:
            self.set_roll_number(roll_number)
        print("Details updated successfully.")

# Testing the implemented functionality
if __name__ == "__main__":
    # Create instances of the Student class
    student1 = Student("Alice", 20, "S1001")
    student2 = Student("Bob", 22, "S1002")

    # Display student information
    print("Student 1 Information:")
    student1.display_info()

    print("\nStudent 2 Information:")
    student2.display_info()

    # Update student details
    print("\nUpdating Student 1 Information...")
    student1.update_details(name="Alicia", age=21)

    print("\nUpdated Student 1 Information:")
    student1.display_info()
