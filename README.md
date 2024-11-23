# Python-Assignment-1
Solution-1:

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def to_uppercase(s):
    return s.upper()

# Moderate Functions
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

def replace_substring(s, old, new):
    return s.replace(old, new)

def split_string(s, delimiter):
    return s.split(delimiter)


# Tough Functions
def join_strings(strings, delimiter):
    return delimiter.join(strings)

def find_substring(s, substring):
    return s.find(substring)

def capitalize_string(s):
    return s.capitalize()



