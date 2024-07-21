# word_counter.py

import os
import string

def count_word_occurrences(filename):
    """
    Reads a text file and counts the occurrences of each word in the paragraph.
    
    Args:
    filename (str): The name of the file to read.
    
    Returns:
    dict: A dictionary with words as keys and their occurrences as values.
    """
    word_counts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                words = line.split()
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {filename}.")
    
    return word_counts

def print_word_counts(word_counts):
    """
    Prints the word counts in alphabetical order.
    
    Args:
    word_counts (dict): A dictionary with words as keys and their occurrences as values.
    """
    for word in sorted(word_counts.keys()):
        print(f"{word}: {word_counts[word]}")

if __name__ == "__main__":
    # Specify the filename
    filename = "19_ques/paragraph.txt"
    
    # Count word occurrences
    word_counts = count_word_occurrences(filename)
    
    # Print word counts
    print_word_counts(word_counts)
