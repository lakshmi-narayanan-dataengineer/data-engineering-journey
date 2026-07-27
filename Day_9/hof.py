"""
Higher-Order Functions in Python
--------------------------------
A Higher-Order Function is a function that either:
1. Takes one or more functions as arguments.
2. Returns a function as its output (Closure).
"""


# 1. Higher-Order Function: Passing a Function as an Argument


def gmail_email(username, domain="gmail.com"):
    """Formats an email address using a default domain."""
    return f"{username}@{domain}"


def build_email(username, email_func):
    """
    Higher-Order Function that accepts a function (email_func)
    as an argument and executes it.
    """
    return email_func(username)


# Usage
user_email = build_email("gowtham", gmail_email)
print("1. Function passed as argument:", user_email)


# 2. Higher-Order Function: Returning a Function as Output (Closure)


def email_builder(domain):
    """
    Higher-Order Function that returns a customized inner function.
    The inner function retains access to 'domain' (Closure).
    """
    def build_email_with_domain(username):
        return f"{username}{domain}"
    
    return build_email_with_domain


# Usage: Factory pattern creating customized email functions
gmail = email_builder("@gmail.com")
outlook = email_builder("@outlook.com")

print("2. Function returned as output (Gmail):", gmail("gowtham"))
print("3. Function returned as output (Outlook):", outlook("gowtham"))