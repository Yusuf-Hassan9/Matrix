
# Represents a car's engine with two attributes:
# engine: Type or name of the engine.
# horse_power: Engine's horsepower rating.


class Engine:
    def __init__(self, engine, horse_power):
        self.engine = engine
        self.horse_power = horse_power


# Represents a car wheel.
# size: Size of the wheel in inches.


class Wheel:
    def __init__(self, size):
        self.size = size

'''
Represents a car tire.
tyre: Type or brand of the tire.
'''

class Tyre:
    def __init__(self, tyre):
        self.tyre= tyre


# Represents a complete car object by,
# composing the previous classes and adding additional functionality:
# make: Manufacturer of the car.
# model: Model name of the car.
# engine: Engine type.
# horse_power: Horsepower of the engine.
# wheels: A list of 4 Wheel objects.
# tyre: Tire type or brand.
# fuel_level: Fuel level in liters (default is 40 liters).


class Car:
    def __init__(self, make, model, engine, horse_power, wheel_size, tyre,
                fuel_level=40.0):
        self.make = make
        self.model = model
        self.engine = engine
        self.horse_power = horse_power
        self.wheels =[Wheel(wheel_size)for wheel in range(4)]
        self.tyre = tyre
        self.fuel_level = fuel_level

    
    # Returns a formatted string describing the car:
    # Manufacturer and model.
    # Engine type and horsepower.
    # Wheel size and tire type.
    

    def display_car(self):
        return f"{self.make} {self.model} - {self.engine} {self.horse_power}(BHp) - {self.wheels[0].size}in {self.tyre}Tyres"

    # Simulates driving the car for a given distance (in miles).
    # Calculates the fuel consumption based on a rate of 0.05 liters per mile.
    # Decreases the fuel_level by the consumed amount.

    def drive(self, distance):
        fuel_consumption = distance * 0.05 
        self.fuel_level -= fuel_consumption

        # Ensure fuel doesn't go negative
        if self.fuel_level < 0:
            self.fuel_level = 0 

        # Displays how much fuel was consumed and the remaining fuel level.
        print(f"You drove {distance} miles and used {fuel_consumption:.2f} Units of Fuel.")
        print(f"Remanining Fuel: {self.fuel_level:.2f} units.\n")

        # If the fuel level is critically low (<1 liter),
        # warns the user and automatically calls the refill_fuel method.

        if self.fuel_level < 1.0:
            print("Warning: Your fuel level is critically low! You need to"
            " refuel.\n")
            self.refill_fuel()

    # Refuel function
    # Handles refueling the car:
    # Prompts the user to choose whether to refill the fuel tank.

    def refill_fuel(self):
        while True:
            decision = input("Do you want to stop at the next fuel station and"
                             " refill your tank?\n[Y]Yes\n[N] No\n").lower()

            # If the user chooses y (yes),
            # refills the fuel tank to full (40 liters) and exits the loop.
            if decision == 'y':
                self.fuel_level = 40.0  # Refill the tank to full (40 liters)
                print(f"Your tank is now full with {self.fuel_level} liters of"
                      " fuel!\n")
                break

            # If the user chooses n (no),
            # displays a warning about running out of fuel and exits the loop.

            elif decision == 'n':
                print("You chose not to refuel. Be careful, you may run out of"
                      " fuel!\n")
                break

            # If the input is invalid, prompts the user to enter a valid choice.

            else:
                print("Invalid input. Please choose [Y] Yes or [N] No.\n")
