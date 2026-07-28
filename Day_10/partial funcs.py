"""
Partial Functions in Python
---------------------------
A Partial Function allows you to fix/freeze a specific number of arguments 
of an existing function, generating a new function with a simplified signature.

This helps avoid repeating the same arguments across multiple function calls.
"""

from functools import partial


# 1. Base Function Definition

def email_build(username, domain):
    """Formats an email address given a username and a domain."""
    return f"{username}@{domain}"

# 2. Creating Partial Functions


# Freeze 'domain' as 'gmail.com' to create a dedicated Gmail generator
gmail = partial(email_build, domain="gmail.com")

# Freeze 'domain' as 'outlook.com' for Outlook addresses
outlook = partial(email_build, domain="outlook.com")



# 3. Usage


print("Gmail Address:", gmail("gowtham"))
# Output: Gmail Address: gowtham@gmail.com

print("Outlook Address:", outlook("gowtham"))
# Output: Outlook Address: gowtham@outlook.com