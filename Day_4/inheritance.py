#Inheritance
#Definition: Inheritance allows a child class to adopt the attributes and methods of a parent class. This enables clean code reuse without rewriting the same logic across multiple classes.

class Vehicle:
    def start(self):
        return "The vehicle's engine is running smoothly."

# Bike inherits everything from Vehicle
class Bike(Vehicle):
    def pop_wheelie(self):
        return "The bike is doing a wheelie!"

# Creating an instance of the child class
my_bike = Bike()

# Using the inherited method from the parent class
print(my_bike.start())       # Output: The vehicle's engine is running smoothly.

# Using the child's unique method
print(my_bike.pop_wheelie()) # Output: The bike is doing a wheelie!




# Polymorphism (Method Overriding)
#Definition: Polymorphism (meaning "many forms") allows different classes to share the exact same method name but execute completely different logic. By overriding a parent class method inside a child class, the child can provide its own specific version of that behavior.

class Vehicle:
    def fuel_type(self):
        return "Uses general fuel."

class ElectricCar(Vehicle):
    # Overriding the parent method to provide specific behavior
    def fuel_type(self):
        return "Uses electricity from a Lithium-ion battery."

class PetrolBike(Vehicle):
    # Overriding the same parent method with a different behavior
    def fuel_type(self):
        return "Uses premium unleaded petrol."

# Testing polymorphism across different object types
vehicles = [ElectricCar(), PetrolBike()]

for v in vehicles:
    # Both objects respond to the exact same method call in their own way
    print(v.fuel_type())
#Output:
#Uses electricity from a Lithium-ion battery.
#Uses premium unleaded petrol.