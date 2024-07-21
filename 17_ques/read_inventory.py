# 

def read_inventory_file(filename):
    """
    Reads and displays the contents of a text file line by line.
    
    Args:
    filename (str): The name of the file to read.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {filename}.")

if __name__ == "__main__":
    # Specify the filename
    filename ="17_ques\inventory.txt "

    # Read and display the file contents
    read_inventory_file(filename)
