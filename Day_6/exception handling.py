#Exception Handling: The process of catching and managing runtime errors (try-except) so that an unexpected failure in one line of code doesn't crash the entire program.

a = 10
b = 0

try:
    result = a / b
    print(result)
except ZeroDivisionError as e:
    # Catches the specific division error cleanly
    print(f"Error Caught: '{e}'. A number cannot be divided by zero!")
finally:
    print("Execution complete: Handled division attempt safely.\n")


#Custom Exceptions: User-defined exception classes (created by inheriting from Python's built-in Exception class) 
#used to enforce custom business logic rules or domain requirements.

class MinimumBalanceError(Exception):
    """Raised when a withdrawal drops the balance below the required threshold."""
    pass


# Step 2: Implement business logic that raises the custom exception
def withdraw_funds(balance, amount, min_required_balance=1000):
    remaining_balance = balance - amount
    
    if remaining_balance < min_required_balance:
        # Manually trigger (raise) our custom exception with a clear message
        raise MinimumBalanceError(
            f"Withdrawal denied! Remaining balance is ${remaining_balance}, "
            f"which is below the required minimum of ${min_required_balance}."
        )
    
    return remaining_balance



account_balance = 1500
withdrawal_amount = 800

try:
    account_balance = withdraw_funds(account_balance, withdrawal_amount)
    print(f"Withdrawal successful! New balance: ${account_balance}")
except MinimumBalanceError as err:
    print(f"Transaction Failed: {err}")
#Output

#Error Caught: 'division by zero'. A number cannot be divided by zero!
#Execution complete: Handled division attempt safely.
#Transaction Failed: Withdrawal denied! Remaining balance would be $700, which is be