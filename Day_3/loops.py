"""
1. For Loop
Definition: A for loop is used when you want to iterate over a sequence 
(like a list, tuple, or range) a predetermined number of times. You know 
the iteration count or sequence length in advance."""

for i in range(1, 10):
    print(i)  # Prints numbers from 1 to 9



"""2. While Loop
Definition: A while loop executes as long as a specified condition remains True. 
It is typically used when the exact number of iterations is NOT known in advance, 
or when waiting for a specific event or target condition to be met."""


nums = [1, 2, 3, 4, 5, 6]
index = 0

while index < len(nums):
    print(nums[index])  # Standard way to print each item sequentially
    index += 1        


"""
3. Continue Statement

Definition: The continue statement skips the rest of the code inside the current 
loop cycle and forces the loop to jump straight to the next iteration."""

for i in range(1, 19):
    if i == 11:
        continue  # Skips printing 11 entirely and jumps straight to 12
    print(i)


"""4. Break Statement
Definition: The break statement completely terminates the loop execution immediately, 
ignoring any remaining items or iterations."""

for i in range(1, 21):
    if i == 20:
        break  # The loop stops  here; 20 is never printed
    print(i)


"""
 5. Pass Statement
Definition: The pass statement is a null operation. It acts as a syntactic 
placeholder when code is required structurally (to avoid syntax errors), 
 but you don't want to execute any code logic yet.
 Note: In your original example, because 'pass' does nothing, 4 was still printed. 
Here is how it is typically used as an empty block placeholder:"""

for i in range(1, 6):
    if i == 4:
        pass  # Handle this specific case later. For now, do nothing.
    print(i)