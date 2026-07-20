#Abstraction
#Definition: Abstraction hides complex implementation details and only exposes essential interfaces. By inheriting from an Abstract Base Class (ABC), we create a mandatory blueprint (contract). 
#Any subclass must override and implement all @abstractmethod definitions, ensuring consistent structure across different classe

from abc import ABC, abstractmethod

# Abstract Base Class (Cannot be instantiated directly)
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        """Mandatory method: Every child class MUST implement this."""
        pass  # Placeholder since abstract methods don't contain implementation logic

class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow!")

class Dog(Animal):
    def make_sound(self):
        print("Dog says: Woof!")
        
    def fetch_ball(self):
        print("The dog is running after the ball!")


cat = Cat()
cat.make_sound()  # Output: Cat says: Meow!

dog = Dog()
dog.make_sound()  # Output: Dog says: Woof!
dog.fetch_ball()  # Output: The dog is running after the ball!

# --- Abstraction Enforcement in Action ---
# 1. Attempting to create an instance of the abstract class directly will crash:
# generic_animal = Animal()  
# TypeError: Can't instantiate abstract class Animal with abstract method make_sound

# 2. If a child class fails to implement make_sound(), Python will throw a TypeError!