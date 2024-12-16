# Base Class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Derived Class: TeslaCar
class TeslaCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity, autopilot_enabled):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity  # in kWh
        self.autopilot_enabled = autopilot_enabled

    def drive(self, distance):
        return f"The Tesla {self.model} drives {distance} miles using its electric motor."

    def activate_autopilot(self):
        if self.autopilot_enabled:
            return "Autopilot activated. Sit back and relax!"
        return "Autopilot is not enabled on this vehicle."

# Example Usage
tesla_model_s = TeslaCar("Tesla", "Model S", 2023, 100, True)
print(tesla_model_s.get_info())
print(tesla_model_s.drive(50))
print(tesla_model_s.activate_autopilot())

class Vehicle:
    def move(self):
        pass  # This will be overridden by child classes

# Subclasses with specific move() behavior
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Polymorphism in action
def demonstrate_movement(vehicle):
    print(vehicle.move())

# Example Usage
car = Car()
plane = Plane()
boat = Boat()

print("Vehicle Actions:")
demonstrate_movement(car)   # Outputs: Driving 🚗
demonstrate_movement(plane) # Outputs: Flying ✈️
demonstrate_movement(boat)  # Outputs: Sailing 🚤
