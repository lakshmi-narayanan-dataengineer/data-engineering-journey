'''Conditional statements allow programs to make decisions. They execute different blocks of code depending on whether a condition evaluates to True or False.
The main keywords are: if, elif, else, and nested if.'''

#Example 1 Only if
#Real-world use case: A school admission form categorizing children by age group.
age = int(input("Enter your age: "))
if age <= 5:
    print("You are a Toddler")
#if → executes code if condition is true  

#Example 2: if-else (Voting Eligibility)
#Real-world use case: Government systems checking if a citizen meets the minimum voting age.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote in the election")
else:
    print("You are not eligible to vote")

#Example 3: if-elif-else (Traffic Signal)
#Real-world use case: A driving simulator applying traffic rules based on signal lights.

signal = input("Enter the signal color: ")
if signal.lower() == "red":
    print("Stop your vehicle for 70 seconds")
elif signal.lower() == "yellow":
    print("Get ready to go")
else:
    print("Go")

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
