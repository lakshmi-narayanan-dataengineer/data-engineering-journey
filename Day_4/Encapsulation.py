#Encapsulation 
#Encapsulation is defined as bundling Variables (Attributes) and method (functions) together inside a class.
#To prevent accidental changes by the user and make the code secure 


class DigitalWallet:
    def __init__(self, owner_name, initial_balance, pin_code):
        self.owner_name = owner_name       # Public attribute (accessible anywhere)
        self._balance = initial_balance    # Protected attribute (internal use suggested)
        self.__pin = pin_code              # Private attribute (hidden via name mangling)

    # Getter: Provides controlled, read-only access to the protected balance
    def get_balance(self):
        return self._balance

    # Setter: Acts as a security checkpoint to validate data before updating
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Successfully deposited ${amount}.")
        else:
            print("Deposit amount must be positive!")



wallet = DigitalWallet("Anu", 50, 1234)

# 1. Reading data safely using the Getter
print(f"Initial Balance: ${wallet.get_balance()}")  # Output: 50

# 2. Updating data safely using the Setter (with validation)
wallet.deposit(100)                                # Output: Successfully deposited $100.
print(f"Updated Balance: ${wallet.get_balance()}")  # Output: 150

# 3. Validation guard in action
wallet.deposit(-20)                                # Output: Deposit amount must be positive!

# 4. Attempting direct private access
# print(wallet.__pin)  # Raises AttributeError: 'DigitalWallet' has no attribute '__pin'