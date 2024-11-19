# Creating The Blueprint for the Cars
# Using COMPOSITION

class Engine:
    def __init__(self, engine, horse_power):
        self.engine = engine
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Tyre:
    def __init__(self, tyre):
        self.tyre= tyre

# Composing previous classes to create my Ultimate Car class
class Car:
    def __init__(self, make, model, engine, horse_power, wheel_size, tyre, fuel_level=40.0):
        self.make = make
        self.model = model
        self.engine = engine
        self.horse_power = horse_power
        self.wheels =[Wheel(wheel_size)for wheel in range(4)]
        self.tyre = tyre
        self.fuel_level = fuel_level

# Choosing what i want it to appear like
    def display_car(self):
        return f"{self.make} {self.model} - {self.engine} {self.horse_power}(BHp) - {self.wheels[0].size}in {self.tyre}Tyres"

    def drive(self, distance):
        fuel_consumption = distance * 0.05  # Fuel consumed per mile
        self.fuel_level -= fuel_consumption
        if self.fuel_level < 0:
            self.fuel_level = 0  # Ensure fuel doesn't go negative
        print(f"You drove {distance} miles and used {fuel_consumption:.2f} Units of Fuel.")
        print(f"Remanining Fuel: {self.fuel_level:.2f} units.\n")

        # Check if fuel is below 1 liter
        if self.fuel_level < 1.0:
            print("Warning: Your fuel level is critically low! You need to refuel.\n")
            self.refill_fuel()

    def refill_fuel(self):
        while True:
            decision = input("Do you want to stop at the next fuel station and refill your tank?\n[Y]Yes\n[N] No\n").lower()
            if decision == 'y':
                self.fuel_level = 40.0  # Refill the tank to full (40 liters)
                print(f"Your tank is now full with {self.fuel_level} liters of fuel!\n")
                break
            elif decision == 'n':
                print("You chose not to refuel. Be careful, you may run out of fuel!\n")
                break
            else:
                print("Invalid input. Please choose [Y] Yes or [N] No.\n")
