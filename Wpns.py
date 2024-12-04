import random

## ALL WEAPON CLASSES - THE MATRIX ##

# PLAYER WEAPONS #

class Weapon1:
    
    def __init__(self, name):
        
                  # Creating the Katana.
        if name == "Katana": 
                self.name = "Katana"
                self.weapon_type = "Blade"
                self.damage = 15

                    # Creating the Pump Shotgun
        elif name == "Pump Shotgun":
                self.name = "Pump Shotgun"
                self.weapon_type = "Gun"
                self.damage = 30
        
                    # Creating the Glock 19
        elif name == "Glock 19":
                self.name = "Glock 19"
                self.weapon_type = "Gun"
                self.damage = 20


# ENEMY WEAPONS #

class Weapon2:                          
    
    def __init__(self, name):

                  # Creating the Atomiser
        if name == "Atomiser":
                self.name = "Atomiser"
                self.weapon_type = "Gun"
                self.damage = random.randrange(19, 26)

                    # Creating the Matrix Rifle
        elif name == "Matrix Rifle":
                self.name = "Matrix Rifle"
                self.weapon_type = "Gun"
                self.damage = 37

                    # Creating the Machine pistol 
        elif name == "Machine pistol":
                self.name = "Machine Pistol"
                self.weapon_type = "Gun"
                self.damage = 18

                    # Creating the Carribean Machete
        elif name == "Carribean machete":
                self.name = "Carribean Machete"
                self.weapon_type = "Blade"
                self.damage = 15

                    # Creating the Myth
        elif name == "Myth":
            self.name = "Myth"
            self.weapon_type = "Gun"
            self.damage = 50

