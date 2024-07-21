# string_utils.py

def reverse_string(s):
    """
    Returns the reverse of the input string s.
    """
    return s[::-1]

def capitalize_string(s):
    """
    Returns the input string s with the first letter of each word capitalized.
    """
    return s.title()

def to_uppercase(s):
    """
    Returns the input string s converted to uppercase.
    """
    return s.upper()

def to_lowercase(s):
    """
    Returns the input string s converted to lowercase.
    """
    return s.lower()

def remove_whitespace(s):
    """
    Returns the input string s with leading and trailing whitespace removed.
    """
    return s.strip()

def remove_punctuation(s):
    """
    Returns the input string s with all punctuation removed.
    """
    import string
    return s.translate(str.maketrans('', '', string.punctuation))
