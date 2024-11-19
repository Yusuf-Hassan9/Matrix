import random

                                                                         ## ALL WEAPON CLASSES - THE MATRIX ##



class Weapon1:                         # PLAYER WEAPONS #
    
    def __init__(self, name):
        
                  # Katana #
        if name == "Katana": 
                self.name = "Katana"
                self.weapon_type = "Blade"
                self.damage = 15

                    # Pump Shotgun #
        elif name == "Pump Shotgun":
                self.name = "Pump Shotgun"
                self.weapon_type = "Gun"
                self.damage = 30
        
                    # Glock 19 #
        elif name == "Glock 19":
                self.name = "Glock 19"
                self.weapon_type = "Gun"
                self.damage = 20




class Weapon2:                         # ENEMY WEAPONS # 
    
    def __init__(self, name):

                  # Atomiser #
        if name == "Atomiser":
                self.name = "Atomiser"
                self.weapon_type = "Gun"
                self.damage = random.randrange(19, 26)

                    # Matrix Rifle #
        elif name == "Matrix Rifle":
                self.name = "Matrix Rifle"
                self.weapon_type = "Gun"
                self.damage = 37

                    # Machine pistol #
        elif name == "Machine pistol":
                self.name = "Machine Pistol"
                self.weapon_type = "Gun"
                self.damage = 18

                    # Carribean Machete #
        elif name == "Carribean machete":
                self.name = "Carribean Machete"
                self.weapon_type = "Blade"
                self.damage = 15

                    # Myth #
        elif name == "Myth":
            self.name = "Myth"
            self.weapon_type = "Gun"
            self.damage = 50

