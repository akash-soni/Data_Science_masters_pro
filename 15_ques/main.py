# main.py

from string_utils import reverse_string, capitalize_string, to_uppercase, to_lowercase, remove_whitespace, remove_punctuation

# Test strings
test_string = "  Hello, World!  "
test_string2 = "python programming"

# Reverse string
reversed_string = reverse_string(test_string)
print(f"Reversed: '{reversed_string}'")

# Capitalize string
capitalized_string = capitalize_string(test_string2)
print(f"Capitalized: '{capitalized_string}'")

# Convert to uppercase
uppercase_string = to_uppercase(test_string2)
print(f"Uppercase: '{uppercase_string}'")

# Convert to lowercase
lowercase_string = to_lowercase(test_string)
print(f"Lowercase: '{lowercase_string}'")

# Remove whitespace
trimmed_string = remove_whitespace(test_string)
print(f"Trimmed: '{trimmed_string}'")

# Remove punctuation
no_punctuation_string = remove_punctuation(test_string)
print(f"No Punctuation: '{no_punctuation_string}'")
