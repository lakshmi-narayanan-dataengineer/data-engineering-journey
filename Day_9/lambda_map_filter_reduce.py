"""
Demonstrating Lambda Functions along with built-in higher-order 
functions: map(), filter(), and reduce().
"""

from functools import reduce


# 1. Lambda Function
# Definition: An anonymous (nameless), single-line function used for 
# short, simple operations without using the traditional 'def' keyword.
# Syntax: lambda arguments: expression


square = lambda x: x * x
print("Square of 45:", square(45))  # Output: 2025


# 2. map()
# Definition: Applies a given transformation function to every item in an 
# iterable (like a list) and returns an updated map object.
# Syntax: map(function, iterable)


fruits = ["apple", "banana", "cherry"]
uppercase_fruits = list(map(lambda fruit: fruit.upper(), fruits))

print("Uppercase Fruits:", uppercase_fruits)  # Output: ['APP', 'BAN', 'CHER']


# 3. filter()
# Definition: Passes each item of an iterable through a conditional 
# function and keeps only the elements that evaluate to True.
# Syntax: filter(function, iterable)

nums = [1, 2, 3, 4, 5, 6, 7]
even_numbers = list(filter(lambda x: x % 2 == 0, nums))

print("Even Numbers:", even_numbers)  # Output: [2, 4, 6]


# 4. reduce()
# Definition: Sequentially applies a function with two arguments to the 
# items of an iterable, accumulating results to reduce it to a single value.
# Syntax: reduce(function, iterable)


sum_of_nums = reduce(lambda total, current: total + current, nums)

print("Sum of Numbers:", sum_of_nums)  # Output: 28