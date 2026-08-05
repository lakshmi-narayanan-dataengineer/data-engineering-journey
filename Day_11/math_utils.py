"""
Math Utility Functions
----------------------
Contains basic mathematical helper functions with robust error handling.
"""

def safe_divide(a, b):
    """
    Divides number 'a' by 'b' with error handling for zero division.
    
    Returns:
        float: The result of a / b.
        str: Error message if b is zero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot Divide By Zero"
    