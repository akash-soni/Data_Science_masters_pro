
# calculate_expenses.py

def calculate_total_expenses(filename):
    """
    Reads a text file containing expenses and calculates the total amount spent.
    
    Args:
    filename (str): The name of the file to read.
    
    Returns:
    float: The total amount spent.
    """
    total = 0.0
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Assuming each line contains an expense amount
                expense = float(line.strip())
                total += expense
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {filename}.")
    except ValueError:
        print(f"An error occurred while parsing an expense amount.")
    
    return total

if __name__ == "__main__":
    # Specify the filename
    filename = "18_ques/expenses.txt"
    
    # Calculate the total expenses
    total_expenses = calculate_total_expenses(filename)
    
    # Print the total expenses
    print(f"Total amount spent: ${total_expenses:.2f}")
