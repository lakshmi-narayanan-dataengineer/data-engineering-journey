# Python String Methods:

"""Strings are immutable sequences of characters in Python. Because they cannot be changed in place, 
these built-in methods are used to transform text data and return clean, new string outputs.
"""

## 1. Merging & Combining: `join()`
#The `join()` method takes an iterable (like a list of words) and merges them into a single string using a specified character string as the connector.

str_1 = "Hello"
str_2 = "World"

# Merge using a space as a separator
joined_str = " ".join([str_1, str_2])
print(joined_str) 
# Output: Hello World

# 2.Modifying and editing : replace()
#The replace() method scans a string for a target substring and swaps it with a new value.
word = "Python is a user friendly Language"

# Swapping 'user' with 'beginner'
replaced_word = word.replace('user', 'beginner')
print(replaced_word)
# Output: Python is a beginner friendly Language

# 3.Advanced Log Extraction :strip() and split()
"""split(separator): Slices a string into a list of strings based on the given separator.
strip(): Shaves off all leading and trailing whitespaces or hidden characters from both edges.
Chaining them allows you to target and cleanly extract pieces of data from long notification text strings."""

given_word = "It is your upcoming rapido ride OTP:1111 , Please Don't share with anyone"

# Sequential execution: Cut by comma -> Keep left block -> Cut by 'ride' -> Keep right block -> Clean spaces
splitted = given_word.split(",")[0].split("ride")[1].strip()

print(splitted)    
# Output: OTP:1111

#4. Case Standardizing: upper(), lower(), & title()
#These methods change the case styles of text blocks. They are critical for processing raw inputs before storing them in database engines.

raw_input = "lAkShMi nArAyAnAn"

print(raw_input.upper())  # Output: LAKSHMI NARAYANAN
print(raw_input.lower())  # Output: lakshmi narayanan
print(raw_input.title())  # Output: Lakshmi Narayanan

#5. Boolean Verification: startswith() & endswith()
#These functions evaluate the prefix or suffix characters of a string, returning a boolean True or False.

filename = "internship_certificate.pdf"
print(filename.endswith(".pdf"))  # Output: True

url = "[https://github.com](https://github.com)"
print(url.startswith("https"))    # Output: True

#6. Location Searching: find() & count()
'''find(substring): Returns the lowest index position where the substring starts. Returns -1 if missing.

count(substring): Calculates how many times a character or phrase repeats inside the string.'''

log_message = "ERROR: Connection timeout at system port 8080. ERROR resolved."

# Locating starting point of the first instance
print(log_message.find("ERROR"))   # Output: 0

# Counting all instances
print(log_message.count("ERROR"))  # Output: 2

#format() method
# When you place curly braces {} inside your string to act as empty placeholders (position indicators). Then, you chain .format() to the end of the string and pass the variables you want to insert inside the parentheses.

# 1. Basic Single Placeholder

name = "Lakshmi"
greeting = "Hello, {}!".format(name)

print(greeting)
# Output: Hello, Lakshmi!

#2. Multiple Placeholders (Ordered by Default)
# If you leave the curly braces empty, Python automatically inserts the arguments in the exact order you pass them from left to right.


role = "Data Engineer"
year = 2026

message = "I am a {}, preparing for my career in {}.".format(role, year)
print(message)
# Output: I am a Data Engineer, preparing for my career in 2026.

"""Advanced Controls with .format()
To prevent mistakes when dealing with complex data pipelines or long log messages, you can explicitly control where each value goes using Index Numbers or Keyword Names.

A. Using Index Numbers (Positional Arguments)
Inside the curly braces, you can write numbers starting from 0. This matches the index layout of the items inside your .format() brackets. This allows you to repeat variables without typing them twice.

"""
# Index positions: 0 = "Python", 1 = "Data"
template = "Learning {0} helps you process {1}. I love {0}!"

result = template.format("Python", "Data")
print(result)
# Output: Learning Python helps you process Data. I love Python!