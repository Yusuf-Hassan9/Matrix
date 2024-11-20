from Fnc import *
from Wpns import *

import random                                                            

## ALL CHARCACTER CLASSES - THE MATRIX ##

class Character:
    def __init__(self, name, HP, strength):
        self.name = name
        self.HP = HP
        self.strength = strength
        self.weapon = ""
        self.car = ""
        self.powerup = 100

    # Feature For Player to Attack using Strength
    def attack(self,target):
        sprint("you throw a powerful punch, landing a solid hit on the"
               " Henchman's jaw!\n")
        # Enemy Deals Damage
        target.HP -= random.randrange( 15 , 20 )

        # Using Weapon To Fight
    def weapon1_attack(self ,target):
        sprint("You have landed a shot!\n")
        # Enemy Deals Damage
        target.HP -= self.weapon.damage

    # The Powerup
    def powerup_attack(self, target):
        print("You have become unstoppable.\n")
        print("You dodge every bullet. Your Oppenet is now fearful. You have"
              " striked the opponent.\n")
        target.HP -= self.powerup

    # Player Health Check
    def health_check(self):
        # Showing The Players Current Health
        print("Your Health Check : \n", self.HP)
        # Players Health Below 0 Means they Die and Fail
        if self.HP <= 0:
            print(f"{player.name} You have died \n")
            sprint("\n====== MISSION FAILED ======\n")
            battle = False
            exit()

    # Supermarket Feature
    def increase_hp(self, amount):
        self.HP += amount
        if self.HP < 100:  # Assuming 100 is the maximum HP cap
            self.HP = 100
        print(f"{self.name}'s HP increased to {self.HP}.\n")

    def visit_supermarket(self):
        print("Welcome to the supermarket. Choose food or drink to"
              " re-energize:\n")
        supermarket_items = [
            ("Extra Strawberry", 5),
            ("Monster Energy", 10),
            ("Mccoys Flamed Grilled Steak", 3),
            ("Red Bull", 7),
            ("Meal Deal", 15)
        ]

        print(f"{'Item':<25}{'HP Gain'}")
        for idx, (item, HP_increase) in enumerate(supermarket_items, 1):
            print(f"[{idx}] {item:<25}{HP_increase}")

        # error validation
        try:
            choice = int(input("\nChoose an item by entering the number:\n ")) - 1
            if 0 <= choice < len(supermarket_items):
                item_name, HP_increase = supermarket_items[choice]
                print(f"\nYou chose {item_name}, which increases your HP by"
                     f"{HP_increase}.")
                self.increase_hp(HP_increase)
            else:
                print("\nInvalid choice. Please select a valid item number.\n")

        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

class Henchman:
    def __init__(self, name):
        self.name = name
        self.HP = random.randrange( 65 , 80 )
        self.strength = random.randrange( 7 , 17 )
        self.weapon = Weapon2("Carribean machete")

     # Letting the enemy attack with their weapon
    def weapon2_attack(self ,target):
        print("You Have Been Critically Damaged with a Weapon \n")
        target.HP -= self.weapon.damage

    # Letting the enemy attack with their given strength
    def attack(self,target):
        target.HP -= self.strength

    # Enemy Health Check
    def health_check(self):
        print("Henchman Health Check : \n", self.HP)
        if self.HP <= 0:
            print("Congratulations You have Defeated the Henchman\n\n")
            player.HP += random.randrange(45 , 50)
            battle = False

# Final Boss Henchman Class
class Boss:
    def __init__(self, name):
        self.name = name
        self.HP = 110
        self.strength = 10
        self.weapon = Weapon2("Machine pistol")

    # Henchman Boss Attacking with Strength
    def attack(self,target):
        print("You have been Hit!\n")
        target.HP -= 10

    # Henchman Boss Attacking With Weapon
    def weapon2_attack(self ,target):
        print("You Have Been Critically Damaged with a Weapon.\n")
        target.HP -= self.weapon.damage

    # Henchman Boss Healthcheck
    def health_check(self):
        print("Henchman Boss Health Check : \n", self.HP)
        if self.HP <= 0:
            print("Henchman Boss Defeated")
            sprint(f"congratulations {player.name} You have Won the Battle "
                   "Against the Henchman \n")
            player.HP += 50
            battle = False

class Matrix_Guard:
    def __init__(self, name):
        self.name = name
        self.HP = random.randrange(45, 50)
        self.strength = 10
        self.weapon = Weapon2("Atomiser")

# Allowing the Matrix Guard to attack with Weapon
    def weapon2_attack(self,target):
        sprint("The Matrix Guard has hit you with his weapon!\n")
        target.HP -= self.weapon.damage

# Allowing the Matrix Guard to attack with strength
    def attack(self,target):
        target.HP -= self.strength

# Matrix Guard Health Check
    def health_check(self):
        print("Matrix Guard health check :\n", self.HP)
        if self.HP <= 0:
            sprint("You have Defeated the Matrix Guard.\n\n")
            player.HP += random.randrange(46, 52)
            battle = False

# Matrix Agents
class Matrix_Agents:
    def __init__(self, name):
       self.name = name
       self.HP = random.randrange(89, 97)
       self.strength = 30
       self.weapon = Weapon2("Matrix Rifle")


    # Matrix Agents Weapon attack
    def attack(self,target):
        target.HP -= self.strength
        print("You have been punched by the Matrix Agent.\n")

    # Matrix Agent Weapon Attack
    def weapon2_attack(self,target):
        print("You have dealt damage with a Matrix Rifle!\n")
        target.HP -= self.weapon.damage

    # Matrix Agents Health Check
    def health_check(self):
        print("Matrix Agent health check :\n", self.HP)
        if self.HP <= 0:
            sprint("You have terminated a Matrix Agent.\n\n")
            player.HP += random.randrange(54, 60)
            battle = False

# Agent Myth's Character
class Agent_Myth:
    def __init__(self, name):
        self.name = name
        self.HP = 150
        self.strength = 40
        self.weapon = Weapon2("Myth")

    # Agent Myth Attack!
    def attack(self,target):
        target.HP -= self.strength
        print("Agent Myth has Uppercutted you!\n")

    # Myth Weapon Attack
    def weapon2_attack(self,target):
        print("You have been Hit by Myth's Weapon!\n")
        target.HP -= self.weapon.damage

    # Myth Health Check
    def health_check(self):
        print("Agent Myth health check :\n", self.HP)
        if self.HP <= 0:
            sprint("Agent Myth was Defeated!\n\n")
            player.HP += random.randrange(200)
            battle = False



agent_myth = Agent_Myth("Agent Myth")

# The Henchman Boss
henchman = Boss("Matrix Henchman Final Boss")

# Creating Two Henchman Easy
matrix_henchman = []

for i in range(2):
    matrix_henchman.append( Henchman("Matrix Henchman"))



Matrix_agent = []
for i in range(2):
    Matrix_agent.append( Matrix_Agents("Matrix Agent"))

matrix_guard = Matrix_Guard("Matrix Guard")

player = Character(input("What is your name player :\n "), 100 , 25)


# Looping Until Player name is given
while player.name == "":
    print("Invalid Option \n")
    player.name = input("what is your name player:\n ")
else:
    sprint(f"Welcome To the Matrix {player.name} \n")
