#Logging is the practice of recording system events, runtime errors, and operational status to external files 
# (.log or .txt). Unlike standard print() statements—which disappear as soon as the program closes—log files persist on disk. This allows developers and system administrators to audit application behavior, debug issues, and inspect past execution errors asynchronously.


import logging

# 1. Configure the global logger settings
# Defines where to save logs, the minimum severity level to record, and output format.

logging.basicConfig(filename="user_logs.txt" , level=logging.ERROR)


# 2. Define a custom domain exception for business logic rule violations
class LateLoginError(Exception):
    """Raised when an employee logs in past the scheduled start time."""
    pass


# 3. Simulate user inputs (24-hour format: e.g., 9 for 09:00, 10 for 10:00)
user_id = input("Enter your User ID: ")
user_login_time = int(input("Enter your login time (24-hour format, e.g., 10): "))
expected_login_time = int(input("Enter official company login time (e.g., 9): "))


# 4. Enforce business rules and handle log writing
try:
    if user_login_time > expected_login_time:
        # Calculate how many hours late the user was
        hours_late = user_login_time - expected_login_time
        
        # Explicitly raise custom exception with contextual information
        raise LateLoginError(f"Late check-in detected by {hours_late} hour(s).")
    
    print(f"Success: User '{user_id}' logged in on time.")

except LateLoginError as err:
    # Calculate delay for output formatting
    delay = user_login_time - expected_login_time
    
    # Write error details cleanly to 'user_logs.txt'
    logging.error(f"User ID: '{user_id}' | {delay} hour(s) late | Details: {err}")
    print(f"Warning issued to User '{user_id}'. Incident recorded to log file.")

except ValueError:
    # Catches non-integer inputs cleanly without crashing the script
    print("Invalid input: Please enter hours using whole numbers (e.g., 9, 10).")