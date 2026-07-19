#Classes and Objects
# Definition: A class is a structural blueprint (template) that defines the 
# attributes (data) and behaviors (methods) that an object will have. 
# An object is a distinct, physical instance created from that blueprint.

class SmartLight:
    # The Constructor: Sets up the unique data for each individual light bulb
    def __init__(self, room_name, bulb_color):
        self.room = room_name       # Unique attribute for each object
        self.color = bulb_color     # Unique attribute for each object
        self.is_on = False          # Shared baseline state (starts turned off)

    # Method: Represents a real-world action or behavior
    def turn_on(self):
        self.is_on = True
        return f"The {self.color} light in the {self.room} is now turned ON!"

# Creating Instances (Objects) from the Blueprint
# Object 1: Living Room Light
living_room_light = SmartLight("Living Room", "Warm White")

# Object 2: Bedroom Light
bedroom_light = SmartLight("Bedroom", "Neon Blue")


print(living_room_light.turn_on())  
# Output: The Warm White light in the Living Room is now turned ON!

print(bedroom_light.turn_on())      
# Output: The Neon Blue light in the Bedroom is now turned ON!