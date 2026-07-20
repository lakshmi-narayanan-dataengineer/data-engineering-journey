#Class Method (@classmethod): Binds to the class itself rather than a specific object instance. It receives cls as its first parameter and can access or modify class-level state that affects all instances.
#Static Method (@staticmethod): Does not receive an implicit first argument (self or cls). It is an isolated utility function scoped inside a class because it logically belongs there, but it operates independently of class or instance data.

class Vehicle:
    # Class-level attribute (shared by all vehicles)
    brand_name = "Yamaha"

    @classmethod
    def update_brand(cls, new_brand):
        """Modifies class state. Affects the entire class factory."""
        cls.brand_name = new_brand

class SpeedUtility:

    @staticmethod
    def kph_to_mph(kph):
        """Self-contained utility helper. Needs no access to class or instance data."""
        return kph * 0.621371


# --- 1. Class Method Usage ---
print(f"Original Brand: {Vehicle.brand_name}")  # Output: Yamaha

# Update the brand at the class level
Vehicle.update_brand("KTM")
print(f"Updated Brand: {Vehicle.brand_name}")   # Output: KTM


# --- 2. Static Method Usage ---
# Convert speed without needing to instantiate an object or alter class state
speed_mph = SpeedUtility.kph_to_mph(100)
print(f"100 KPH in MPH: {speed_mph:.2f}")        # Output: 62.14 MPH