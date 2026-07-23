#List Comprehension offers a concise, elegant, and readable syntax for creating new lists based on existing iterables (like ranges, lists, or tuples). It replaces verbose for loops with single-line expressions, 
# aking code more pythonic and execution slightly faster.
result = [x for x in range(10)]
print(result)


# ==============================================================================
# File: list_comprehensions.py
# Purpose: Demonstrating List Comprehension Patterns in Idiomatic Python
# ==============================================================================

# 1. Basic Generation
# Generates numbers 0 through 9
numbers = [x for x in range(10)]
print("Basic Range:", numbers)


# 2. Transformation / Expression
# Calculates squares of numbers from 1 through 20
squares = [x**2 for x in range(1, 21)]
print("Squares (1-20):", squares)


# 3. Filtering with Single 'if' Condition
# Filters out even numbers; keeps only odd numbers between 2 and 23
odds = [x for x in range(2, 24) if x % 2 != 0]
print("Odd Numbers:", odds)


# 4. Conditional Transformation with 'if-else' (Ternary Operator)
# Replaces each number from 10 to 120 with "even" or "Odd"
even_odd_labels = ["even" if x % 2 == 0 else "Odd" for x in range(10, 121)]
print("First 6 Labels:", even_odd_labels[:6])  # Truncated for clean terminal output


# 5. Multiple Nested 'if' Conditions (AND Logic)
# Keeps numbers divisible by BOTH 2 and 3 (i.e., multiples of 6) from 3 to 44
divisible_by_two_and_three = [x for x in range(3, 45) if x % 2 == 0 if x % 3 == 0]
print("Divisible by 2 and 3:", divisible_by_two_and_three)


# 6. Paired Comprehension using zip()
# Combines two separate lists into a list of paired tuples
names = ["anu", "abi", "akshay"]
marks = [23, 45, 78]

student_scores = [(n, m) for n, m in zip(names, marks)]
print("Student Scores:", student_scores)