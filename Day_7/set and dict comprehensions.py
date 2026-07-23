#Dictionary Comprehension: A concise, single-line syntax for constructing dictionaries ({key: value}) by transforming 
# or filtering elements from an iterable.
# ==============================================================================
# File: dict_and_set_comprehensions.py
# Purpose: Clean examples of Dictionary and Set Comprehensions in Python
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. DICTIONARY COMPREHENSIONS
# Syntax: {key_expression: value_expression for item in iterable}
# ------------------------------------------------------------------------------

# Basic Mapping (Without 'if')
# Maps numbers 0 to 4 to their squares
squares_dict = {x: x * x for x in range(5)}
print("Squares Dict:", squares_dict)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# Filtering with 'if'
# Keeps only even numbers as keys from range(15)
even_squares_dict = {x: x * x for x in range(15) if x % 2 == 0}
print("Even Squares Dict:", even_squares_dict)
# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64, 10: 100, 12: 144, 14: 196}


# Conditional Logic with 'if-else' (Ternary Operator)
# Categorizes numbers 1 to 50 as 'is Even' or 'is odd'
parity_dict = {x: "is Even" if x % 2 == 0 else "is odd" for x in range(1, 51)}
print("Sample Parity Dict (1 to 5):", {k: parity_dict[k] for k in range(1, 6)})
# Output: {1: 'is odd', 2: 'is Even', 3: 'is odd', 4: 'is Even', 5: 'is odd'}

#Set Comprehension: A concise syntax for building sets ({value}) that automatically enforces uniqueness 
#  and eliminates duplicate items during construction.

# ------------------------------------------------------------------------------
# 2. SET COMPREHENSIONS
# Syntax: {expression for item in iterable}
# Purpose: Automatically removes duplicates and creates an unordered set of unique items.
# ------------------------------------------------------------------------------

# Input list containing multiple duplicate values
raw_numbers_list = [11, 1, 22, 11, 33, 4, 4, 51, 4, 5, 66, 4, 6, 7, 6, 77, 77, 88, 98, 88]

# Set comprehension filters duplicates dynamically
unique_numbers_set = {num for num in raw_numbers_list}
print("Unique Set from List:", unique_numbers_set)


# Set comprehension with conditional filtering
# Extracts only unique even numbers from the raw list
unique_even_set = {num for num in raw_numbers_list if num % 2 == 0}
print("Unique Even Set:", unique_even_set)