"""
Closure Functions in Python
---------------------------
A Closure occurs when a nested (inner) function remembers and retains access 
to variables from its enclosing (outer) function's scope, even after the outer 
function has finished executing.

Key Requirements:
1. Must have a nested function (a function inside a function).
2. The nested function must refer to a value defined in the enclosing scope.
3. The enclosing function must return the nested function object.
"""

# 1. Defining the Closure Pattern

def create_email_generator(domain):
    """
    Outer function that captures the 'domain' variable in its scope.
    """
    def gen_email(username):
        """
        Inner function (Closure) that uses 'username' along with the 
        enclosing 'domain' variable.
        """
        return f"{username}@{domain}"
    
    return gen_email  # Returning the function object without calling it


# 2. Instantiating and Using Closures


# 'gmail_builder' now holds 'gen_email' with 'domain' pre-configured as "gmail.com"
gmail_builder = create_email_generator("gmail.com")

# Call the closure with the username argument
user_email = gmail_builder("lakshminarayanan")

print("Generated Email:", user_email)
# Output: Generated Email: lakshminarayanan@gmail.com


# Reusability Example: Easily create another specialized generator
yahoo_builder = create_email_generator("yahoo.com")
print("Yahoo Email:", yahoo_builder("lakshminarayanan"))
# Output: Yahoo Email: lakshminarayanan@yahoo.com