"""List
Definition: A mutable, ordered, index-based collection.
Supports operations like insertion, deletion, append, update."""

# Example 1: Simple list
numbers = [10, 20, 30]
print(numbers)  # [10, 20, 30]

# Example 2: Mixed data types
mixed = [1, "apple", 3.5, [2, 4]]
print(mixed)  # [1, 'apple', 3.5, [2, 4]]

# Insertion
numbers = [10, 20, 30]
numbers.insert(1, 15)   # Insert 15 at index 1
print(numbers)  # [10, 15, 20, 30]

# Append
numbers.append(40)
print(numbers)  # [10, 15, 20, 30, 40]

# Update
numbers[2] = 25
print(numbers)  # [10, 15, 25, 30, 40]

# Deletion
numbers.remove(15)
print(numbers)  # [10, 25, 30, 40]


"""Tuple
Definition: An immutable, ordered collection.
Cannot be updated, but supports indexing, slicing, and membership tests.
Faster than lists because of immutability."""

# Example 1: Simple tuple
coordinates = (10, 20)
print(coordinates)  # (10, 20)

# Example 2: Mixed data types
student = ("Arun", 21, "CS")
print(student)  # ('Arun', 21, 'CS')

# Example 3: Nested tuple
nested = (1, (2, 3), 4)
print(nested)  # (1, (2, 3), 4)

# Indexing
coordinates = (10, 20, 30)
print(coordinates[1])  # 20

# Slicing
print(coordinates[:2])  # (10, 20)

# Membership test
print(30 in coordinates)  # True


"""Set
Definition: An unordered, mutable collection of unique elements.
Supports union, intersection, difference, add, remove.
No duplicates allowed.
Useful for membership tests and removing duplicates."""


# Example 1: Simple set
fruits = {"apple", "banana", "cherry"}
print(fruits)  # {'apple', 'banana', 'cherry'}

# Example 2: Removing duplicates
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}

# Example 3: Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))      # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}

# Add
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # {'apple', 'banana', 'cherry'}

# Remove
fruits.remove("banana")
print(fruits)  # {'apple', 'cherry'}

# Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}

# Intersection
print(a.intersection(b))  # {3}

# Difference
print(a.difference(b))  # {1, 2}

"""Dictionary
Definition: A mutable, unordered collection of key-value pairs.

Supports insertion, update, deletion, and iteration."""


# Example 1: Simple dictionary
student = {"name": "Arun", "age": 21}
print(student)  # {'name': 'Arun', 'age': 21}

# Example 2: Updating dictionary
student["course"] = "Python"
print(student)  # {'name': 'Arun', 'age': 21, 'course': 'Python'}

# Example 3: Nested dictionary
students = {
    1: {"name": "Arun", "age": 21},
    2: {"name": "Priya", "age": 22}
}
print(students[2]["name"])  # Priya


# Insertion
student = {"name": "Arun", "age": 21}
student["course"] = "Python"
print(student)  # {'name': 'Arun', 'age': 21, 'course': 'Python'}

# Update
student["age"] = 22
print(student)  # {'name': 'Arun', 'age': 22, 'course': 'Python'}

# Deletion
del student["course"]
print(student)  # {'name': 'Arun', 'age': 22}

# Iteration
for key, value in student.items():
    print(key, ":", value)
# Output:
# name : Arun
# age : 22
