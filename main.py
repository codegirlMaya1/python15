class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"The owner has been updated to {self.owner}")

# Creating two instances of the Vehicle class
vehicle1 = Vehicle("ABC123", "Car", "Alice")
vehicle2 = Vehicle("XYZ789", "Truck", "Bob")

# Displaying initial owners
print(f"Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

# Updating the owner of vehicle1
vehicle1.update_owner("Charlie")

# Updating the owner of vehicle2
vehicle2.update_owner("Dave")

# Displaying updated owners
print(f"Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")