"""
Python Generators & The yield Keyword
------------------------------------
A Generator function creates an iterator on the fly using the 'yield' keyword.
Instead of returning a full dataset at once, it yields values one at a time 
and pauses its execution state until the next value is requested.
"""

# 1. Generator Function Definition


def gen_nums(n):
    """
    Generates numbers from 0 up to n - 1.
    
    Memory Efficiency:
    Unlike returning a full list (e.g., list(range(n))), this function 
    only holds a single number in memory at any given moment.
    """
    for i in range(n):
        yield i  # Pauses function execution and returns the current value of 'i'


# 2. Consuming Generators


# Approach A: Using a for loop (Most Common)
# The loop automatically calls Python's internal next() function on the generator.
print("--- Iterating with a for loop ---")
for num in gen_nums(7):
    print(num)


# Approach B: Using next() manually
# Demonstrates how Python consumes the generator step-by-step under the hood.
print("\n--- Fetching values manually using next() ---")
numbers = gen_nums(3)

print(next(numbers))  # Yields 0, then pauses
print(next(numbers))  # Resumes, yields 1, then pauses
print(next(numbers))  # Resumes, yields 2, then pauses
# Calling next(numbers) again now would raise a StopIteration exception.