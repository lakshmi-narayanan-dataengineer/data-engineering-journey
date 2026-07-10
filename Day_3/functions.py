"""Functions
Definition
A function is a block of reusable code that performs a specific task.
Functions help avoid repetition, make code modular, and allow passing values (arguments) to produce results."""

#Example 1: Basic Function
# Function definition: takes two arguments and returns their sum

def add(a, b):
    return a + b   # 'return' sends the result back to the caller

# Function call
result = add(12, 24)
print("Sum of two numbers:", result)  # Output: 36


#Example 2: *Using args (Unlimited Arguments)
# *args allows passing unlimited positional arguments

def add(*args):
    return sum(args)   # sum() adds all values inside the tuple 'args'

# Function call with multiple numbers
result = add(12, 23, 34, 45)
print("Total sum:", result)  # Output: 114


#Example 3: **Using kwargs (Keyword Arguments as Dictionary)
# **kwargs allows passing key-value pairs (like a dictionary)
def student_info(**kwargs):
    # kwargs is a dictionary, so we can access values by keys
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function call with keyword arguments
student_info(name="Arun", age=20, course="Python Programming")
"""Output
name: Arun
age: 20
course: Python Programming """