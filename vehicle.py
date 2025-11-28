# ----------- 
# Base Class : Vehicles 
# -----------

class Vehicle: 
    vehicle_type = "Generic Vehicle"

    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year 
        self.mileage = mileage  # Protected attribute 

    def drive(self, distance):
        """Increase mileage by distance."""
        if distance > 0:
            self.mileage += distance 

    def get_info(self):
        return f"{self.year} {self.make} {self.model} | Mileage: {self.mileage} km"

    def __str__(self):
        return f"{self.vehicle_type}: {self.get_info()}"

    @classmethod 
    def from_string(cls, text):
        """"Create a Vehicle from string 'Make-Model-Year' """
        make, model, year = text.split('-')
        return cls(make, model, int(year))


# --------
# Subclass : Car 
# -------- 

class Car(Vehicle):
    vehicle_type = "Car"

    def __init__(self, make, model, year, fuel_capacity, mileage=0):
        super().__init__(make, model, year, mileage)
        self.fuel_capacity = fuel_capacity

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Fuel Capacity: {self.fuel_capacity} L"


# --------
# Subclass : ElectricScooter 
# -------- 
class ElectricScooter(Vehicle):
    vehicle_type = "Electric Scooter"

    def __init__(self, make, model, year, battery_percentage=100, mileage=0):
        super().__init__(make, model, year, mileage)
        self.battery_percentage = battery_percentage 

    def drive(self, distance):
        """Driving reduces battery percentage."""
        super().drive(distance)
        # Reduce battery based on distance (simple formula: 1% per 5 km -> 0.2% per km)
        self.battery_percentage = max(0, self.battery_percentage - distance * 0.2)

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Battery: {self.battery_percentage:.1f}%"

    @staticmethod 
    def is_charging_required(battery_percentage):
        """Check if charging is required."""
        return battery_percentage < 20

# --------
# Polymorphic function
# --------

def print_vehicle_report(vehicles):
    for v in vehicles:
        print(v.get_info())  # Polymorphic call


# ---------
# SAMPLE USAGE 
# ---------

vehicles = [
    Car("Toyota", "Corolla", 2020, 50),
    ElectricScooter("Xiaomi", "M365", 2021, 85),
    Vehicle.from_string("Honda-Civic-2019")
]

# Drive each vehicle
for v in vehicles:
    v.drive(100) # Drive each vehicle for 100 km

# Print report
print_vehicle_report(vehicles)

# Check charging needed
scooter = vehicles[1]
print("\nScooter needs charging", ElectricScooter.is_charging_required(scooter.battery_percentage))