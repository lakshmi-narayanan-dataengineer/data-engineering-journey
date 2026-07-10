'''Conditional statements allow programs to make decisions. They execute different blocks of code depending on whether a condition evaluates to True or False.
The main keywords are: if, elif, else, and nested if.'''

#Example 1 Only if
#Real-world use case: A school admission form categorizing children by age group.
age = int(input("Enter your age: "))
if age <= 5:
    print("You are a Toddler")
#if → executes code if condition is true  
#Output Enter your age: 5 , You are a toddler

#Example 2: if-else (Voting Eligibility)
#Real-world use case: Government systems checking if a citizen meets the minimum voting age.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote in the election")
else:
    print("You are not eligible to vote")

"""Output
Case 1: Age ≥ 18

Enter your age: 20
Condition age >= 18 is True, so the output is:
You are eligible to vote in the election 

Case 2: Age < 18
Enter your age: 15
Condition age >= 18 is False, so the else block runs:

You are not eligible to vote
"""

#Example 3: if-elif-else (Traffic Signal)
#Real-world use case: A driving simulator applying traffic rules based on signal lights.

signal = input("Enter the signal color: ")
if signal.lower() == "red":
    print("Stop your vehicle for 70 seconds")
elif signal.lower() == "yellow":
    print("Get ready to go")
else:
    print("Go")

"""Output
Input: red
Stop your vehicle for 70 seconds

Input: yellow
Get ready to go

Input: green (or any other color)
Go
"""
#Example 4: Nested if (License Checker)
#Real-world use case: Transport department system validating both age and license before issuing a driving permit.

age = int(input("Enter your age: "))
license = input("Do you have a license? Type Yes/No: ")

if age >= 18:
    if license.lower() == "yes":
        print("You are eligible to drive")
    else:
        print("Please take a license to drive")
else:
    print("You are not eligible to drive")

"""
Output
Case 1
Age ≥ 18 and License = Yes
You are eligible to drive

Case 2
Age ≥ 18 and License = No
Please take a license to drive

Case 3
Age < 18 (any license input)
You are not eligible to drive
"""

