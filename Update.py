# Creating Character Classes And Battle System Origin
import random

from Door_hack import *
from os import name
from Utilitiespy import *
from Constants import *
from Cars import *
from Weapons2 import *
from MG_battle import *

# Making The Battle a thing
battle = True

# Import First _Battle
    # Creating the player and their stats/features
class Character:
    def __init__(self, name, HP, strength):
        self.name = name
        self.HP = HP
        self.strength = strength
        self.weapon = ""
        self.car = ""
    # Feature For Player to Attack using Strength
    def attack(self,target):
        sprint("you throw a powerful punch, landing a solid hit on the Henchma"
               "n's jaw!\n")
        # Enemy Deals Damage
        target.HP -= random.randrange( 15 , 20 )

        # Using Weapon To Fight
    def weapon1_attack(self ,target):
        print("You Hit a Henchman with a Weapon!")
        # Enemy Deals Damage
        target.HP -= self.weapon.damage

    # Player Health Check
    def health_check(self):
        # Showing The Players Current Health
        print("Your Health Check : \n", self.HP)
        # Players Health Below 0 Means they Die and Fail
        if self.HP <= 0:
            print(f"{player.name} You have died \n")
            sprint("Mission Failed")
            battle = False
            exit()

    def increase_hp(self, amount):
        self.HP += amount
        if self.HP >50:
           self.HP = 100
        print(f"{self.name}'s HP increased to {self.HP}.\n")

    def visit_supermarket(self):
        sprint("Welcome to the Supermarket. Choose food or drink to Re-Energize"
              ": \n")
        supermarket_items = [
            ("Extra Strawberry", 5),
            ("Monster Energy", 10),
            ("Mccoys Flamed Grilled Steak", 3),
            ("Red Bull", 7),
            ("Meal Deal", 15)
        ]

        print(f"{'Item':<25}{'HP Gain'}")
        for idx, (item, hp_increase) in enumerate(supermarket_items, 1):
            print(f"[{idx}] {item:<25}{hp_increase}")

        try:
            Move = int(input("\nChoose an Item by entering a Number:\n ")) - 1
            if 0 <= Move < len(supermarket_items):
                item_name, hp_increase = supermarket_items[Move]
                print(f"\nYou Chose {item_name}, Which increases your health b"
                      f"y {hp_increase}.")
                self.increase_hp(hp_increase)
            else:
                print("\nInvalid Choice. Please select a Valid number.\n")
        except ValueError:
            print("\nInvalid Input. Please enter a number.\n")


 # Creating the Henhchman Stats/Features
class Henchman:
    def __init__(self, name):
        self.name = name
        self.HP = random.randrange( 65 , 80 )
        self.strength = random.randrange( 7 , 17 )
        self.weapon = Weapon1("Carribean machete")

     # Letting the enemy attack with their weapon
    def weapon1_attack(self ,target):
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
        self.weapon = Weapon1("Machine pistol")

    # Henchman Boss Attacking with Strength
    def attack(self,target):
        print("You have been Hit!\n")
        target.HP -= 10

    # Henchman Boss Attacking With Weapon
    def weapon1_attack(self ,target):
        print("You Have Been Critically Damaged with a Weapon \n")
        target.HP -= self.weapon.damage

    # Henchman Boss Healthcheck
    def health_check(self):
        print("Henchman Boss Health Check : \n", self.HP)
        if self.HP <= 0:
            print("Henchman Boss Defeated")
            sprint(f"congratulations {player.name} You have Won the Battle Aga"
                   "inst the Henchman \n")
            player.HP += 50
            battle = False

# Weapon Classes
class Weapon1:
    # Make Weapons 
    def __init__(self, name):
        # Katana
        if name == "Katana":
                self.name = "Katana"
                self.weapon_type = "Blade"
                self.damage = 15
        # Pump Shotgun
        elif name == "Pump Shotgun":
                self.name = "Pump Shotgun"
                self.weapon_type = "Gun"
                self.damage = 30
        # Machine Pistol
        elif name == "Machine pistol":
                self.name = "Machine Pistol"
                self.weapon_type = "Gun"
                self.damage = 18
        # Carribean Machete
        elif name == "Carribean machete":
                self.name = "Carribean Machete"
                self.weapon_type = "Blade"
                self.damage = 15
        # Glock 19
        elif name == "Glock 19":
                self.name = "Glock 19"
                self.weapon_type = "Gun"
                self.damage = 20

# End of Import

# Starting Up The Matrix
start=True

# Getting player name
player = Character(input("What is your name player  :\n "), 100 , 25)

# Looping Until Player name is given
while player.name == "":
    print("Invalid Option \n")
    player.name = input("what is your name player:\n ")
else:
    sprint(f"Welcome To the Matrix {player.name} \n")

# When Player Gives Their name the game starts up
answer = input("Would You like to Take on the Matrix: Yes or No \n").lower()
if answer == "yes":
    sprint("Game Loading.... Game Loading.... Game Loading.... Game Loading..."
           ".\n")

elif answer == "No":
    sprint("Maybe Next time")
    exit()

else:
    print("Please enter yes or no.")
    answer = input("Would You like to Take on the Matrix: Yes or No \n")

Ascii_art1()
print(f"{ai}\n")
sprint(f"{player.name}")



sprint("Time : 11:00am ")
sprint("Location : 9291 Burton Way, Beverly Hills\n")

# The Fisrt Speech
print(f"{npc}\n")
sprint(f"'Dear {player.name},'\n")
sprint("'By the time you are reading this message, The Matrix would have taken"
      "down The Real World and our Database.'\n")
sprint("'They have located our main headquarters, and this morning they launch"
       "ed a full-scale assault, destroying all our Resources.'\n")
sprint("'I was fortunate enough to escape their henchmen, but I am currently h"
       "iding in a safe house, keeping a low profile.'\n")
sprint("'However, The Matrix has become aware of our knowledge regarding their"
      "secrets and Dark Arts, and they are coming after every member of the Re"
      "al World.'\n")
sprint("'The fate of the Real World and everything we have fought for now rest"
       "s on your shoulders.'\n")
sprint(f"'I believe that you are the only one who possesses the skills to save"
      "us and execute our original mission.'\n")
sprint(f"'{player.name}, you must leave your apartment immediately after readi"
       "ng this.'\n")
sprint("'They will be at your door any second, and time is of the essence. I w"
       "ill provide you with the location to retrieve a car.'\n")
sprint("'You must Grab one of the Cars from the Loction and Locate then head t"
       "o the Matrix Headquarters and retrieve our files before they are destr"
       "oyed.'\n")
sprint("'Once you Retrieve the files from The Matrix you can contact me throug"
       "h this network and i will tell you where to meet me'\n")
sprint("'Good luck; our fate hinges on your success.'\n")
sprint("'Remember, no pressure!'\n")

print(f"{npc}\n")
sprint("Car Location : 155 N Crescent Dr, Beverly Hills \n")

# Storyline
print(f"{hman}\n")
sprint("'Knock Knock Knock Knock'\n")

print(f"{player.name}:\n")
sprint("'uh oh ...'\n")

print(f"{hman}\n")
sprint("'BANG!!!'\n")

print(f"{ai}\n")
sprint("'The Matrix Henchman have arrived at your apartment and broken in.'\n")
sprint("'You must Defeat the Henchman then proceed to the Car Location.'\n")
sprint("'You will be given a selection of weaponry to choose from.'\n")

# Player Chooses Their Weapon
weapon = ""
print(f"{ai}\n")
sprint("'Here is your Weaponry Selection' \n")
print("Choose your Weapon Wisely : \n")
Move1 = input("[A] Glock 19\n[B] Katana\n[C] Pump Shotgun \n\n").lower()
if Move1 == 'a':
    player.weapon = Weapon1("Glock 19")
    print(f"Good Choice",player.name,"\n")
elif Move1 == 'b':
    print("Abit of a Sticky one Styll \n")
    player.weapon = Weapon1("Katana")
else :
    print(f"Hit the Jackpot ",player.name,"\n")
    player.weapon = Weapon1("Pump Shotgun")

# Getting to the Battle
print(f"{hmanb}\n")
sprint("'He's there Take him down!' \n")

print(f"{ai}\n")
sprint(f"One of the Matrix Henchmen is barreling toward you, ready to take you"
      "down!")
sprint(f"'{player.name} Will you Fight the Henchman or Surrender ?'")

print(f"{ai}\n")
Move2 = input("[A] Proceed to Fight\n[B] Surrender \n\n").lower()
while Move2 == "" :
    print("Choose one! You can't escape your fate.")
    Move2 = input("[A] Proceed to Fight\n[B] Surrender \n\n").lower()
if Move2 == 'a' :
    sprint("Good luck "+player.name+" \n")
    
else :
    sprint("'You have perished and failed your mission.'")
    sprint("You will now be taken to the start \n")
    exit()

print(f"{ai}\n")
print("These are your stats",player.name ," : \n")
print("HP =",player.HP)
print("Natural Strength =",player.strength,"\n")

# Creating Two Henchman Easy
matrix_henchman = []

for i in range(2):
    matrix_henchman.append( Henchman("Matrix Henchman"))

# matrix_henchman = Enemy("Matrix Henchman "+ str(i+1) , 75, 15)for i in range(2) 
print("This is the Henchman Stats : \n " )
print("HP =",matrix_henchman[0].HP)
print("Strength =",matrix_henchman[0].strength,"\n")

# Matrix Henchman Final Boss

print(f"{ai}\n")
print(f"Its time to Take on the Henchman",player.name,"! \n\n")
input("Press ENTER to continue to battle:  \n\n")
sprint("Proceeding into battle ...   Proceeding into battle ...   Proceeding i"
       "nto battle ...  Proceeding into battle ... \n")

# First Henchman Battle
while battle==True:
    sprint("You find yourself face-to-face with a menacing Henchman.\n")

    # Giving Moves Option
    while True:
        sprint("What will you do?\n")
        print("'Attack' or 'Run'\n")
        sprint("Choose your Move :\n")
        Move3 = input("[A] Attack with Strength \n[B] Attack With Weapon \n[C]"
                     "Run Away \n\n").lower()
        if Move3 == 'a':
            player.attack(matrix_henchman[0])
            break
        elif Move3 == 'b':
            player.weapon1_attack(matrix_henchman[0])
            break
        elif Move3 == 'c':
            matrix_henchman[0].weapon1_attack(player)
            break
        else:
            print("Invalid Choice\n")
            sprint("Choose your Move :\n")
            Move3 = input("[A] Attack with Strength \n[B] Attack With Weapon\n"
                          "\n").lower()

    # Making Player Deal Damage Throughout Battle
    henchman_choice = random.randrange(1,2)

    if henchman_choice == 1:
        matrix_henchman[0].weapon1_attack(player)
    else:
        matrix_henchman[0].attack(player)

    # Battle Health Check (Required)
    matrix_henchman[0].health_check()
    player.health_check()

    # If the Henchman Dies you Can continue
    if matrix_henchman[0].HP <= 0:
        break
     
    # If the Player dies then They have Failed
    if player.HP <= 0:
        exit()

# Storyline
print(f"{hmanb}\n")
sprint("'Impossible How has he Defeated one of us ... !'\n")
sprint("'Finish Him off!!!'\n")

print(f"{ai}\n")
sprint("'You dealt with one Henchman like a true warrior!'\n")
sprint("'But unfortunately, you are nowhere near finished here.'\n")
sprint("'The Henchman Boss has just sent another one of his minions to challen"
       "ge you!'\n")
input("Press ENTER to continue to the next battle:  \n\n")

# Initiate Second Battle
while battle==True:
    sprint("Another Henchman appears, ready to take you down!\n")

    # Giving Moves Option
    while True:
        sprint("What will you do?\n")
        print("'Attack' or 'Run'\n")
        sprint("Choose your Move : \n")
        Move3 = input("[A] Attack with Strength \n[B] Attack With Weapon \n[C]"
                     "Run Away \n\n").lower()
        if Move3 == 'a':
            player.attack(matrix_henchman[1])
            break
        elif Move3 == 'b':
            player.weapon1_attack(matrix_henchman[1])
            break
        elif Move3 == 'c':
            matrix_henchman[1].weapon1_attack(player)
            break
        else:
            print("Invalid Choice\n")
            sprint("Choose your Move :\n")
            Move3 = input("[A] Attack with Strength \n[B] Attack With Weapon\n"
                          "\n").lower()

    # Making Player Deal Damage Throughout the Battle
    henchman_choice = random.randrange(1,2)

    if henchman_choice == 1:
        matrix_henchman[1].weapon1_attack(player)
    else:
        matrix_henchman[1].attack(player)

    # Battle Health Check (Required)
    matrix_henchman[1].health_check()
    player.health_check()

    # If You Defeat Second Henchman Continue
    if matrix_henchman[1].HP <= 0:
        break

    # If the Player dies then They have Failed
    if player.HP <= 0:
        exit()

 # The Henchman Boss
henchman = Boss("Matrix Henchman Final Boss")

# Storyline
print(f"{hmanb}\n")
sprint("'No! This can't be!'\n")
sprint("'Well then... I guess I will have to take matters into my own hands.'"
       "\"n")
sprint("'You will regret going against the Matrix!'\n")

print(f"{ai}\n")
sprint(f"'{player.name} You are Truly One of a kind i must say \n However you "
      "are still a mile away from the taste of temporary Victory.' \n")
sprint(f"'Defeat The Henchman Boss and you shall be the Victor of this Battle!"
       "'\n\n")
sprint(f"Your current Health is {player.HP}\n")
sprint(f"The Henchman Boss health is {henchman.HP}\n")
input("Press ENTER to continue to the final battle:  \n\n")

# Final Henchman Battle (Mini Boss Battle)
while battle==True:
    sprint("The Henchman Boss stands before you, a formidable opponent!\n")
    # Giving Moves Option
    while True:
       sprint("What will you do?\n")
       print("'Attack' or 'Run'\n")
       sprint("Choose your Move : \n")
       Move4 = input("[A] Attack with Strength \n[B] Attack With Weapon \n[C] "
                     "Run Away \n\n").lower()
       if Move4 == 'a':
            player.attack(henchman)
            break
       elif Move4 == 'b':
            player.weapon1_attack(henchman)
            break
       elif Move4 == 'c':
            henchman.weapon1_attack(player)
            break
       else:
            print("Invalid Choice\n")
            sprint("Choose your Move :\n")
            Move4 = input("[A] Attack with Strength \n[B] Attack With Weapon "
                          "\n[C] Run Away \n\n").lower()

# Player Deals Damage Regardless
# Henchman either Attacks Player with Strength or Weapon
    henchman_choice = random.randint(1, 2)

    if henchman_choice == 1:
        henchman.weapon1_attack(player)
    else:
        henchman.attack(player)
        
        # Battle Health Check (Required)
    henchman.health_check()
    player.health_check()

     # Option to get info
    if henchman.HP <= 30:
        break

    # If the Player dies then They have Failed
    if player.HP <= 0:
        exit()

print(f"{hmanb}\n")
sprint("'Oh No I've Been Hit Critically!'\n")
sprint("'The Matrix Will not let you get away with this !!!'\n\n")
print(f"{ai}\n")
sprint(f"'{player.name} You must Get The location of the Matrix Base By tortur"
       "ing this Henchman'\n")
input("Press ENTER to continue :  \n\n")
print(f"{player.name}: \n")
sprint("'Tell me where The Matrix base is or I shall end you'\n")
print(f"{hmanb}\n")
sprint("'Never!\n")
print(f"{player.name}: \n")
sprint("'Fine,you choose Pain'\n")
print(f"{ai}\n")
sprint(f"Make your decision Wisely {player.name} :\n")
Move6 = input("[A] Get Henchman to talk by Waterboarding Him \n[B] Get Henchma"
              "n to talk by Lighting him on Fire\n").lower()
if Move6 == 'a':
     print(f"{hmanb}\n")
     sprint("'Wait Nooo!'")
     sprint("'THE LOCATION IS ..'\n")
     print(f"{player.name}:\n")
     sprint("'SAY IT THEN!'\n")
     print(f"{hmanb}\n")
     sprint("'12th Ave Santa Cruz !'\n")
     print(f"{player.name}:\n")
     sprint("'You just about saved your Life'\n")
     input("Press ENTER to tie up the Matrix Henchman Final Boss :\n")
elif Move6 == 'b':
         print(f"{hmanb}\n")
         sprint("'AAAAAAH'\n")
         sprint("Henchman Final Boss Died.")
         print(f"{ai}\n")
         sprint("Not so Wise \n")
         sprint("Mission Over")
         exit()
else:
    print("Inavlid Choice\n")
    Move6 = input("[A] Get Henchman to talk by Waterboarding Him \n[B] Get Hen"
                  "chman to talk by Lighting him on Fire\n").lower()

# Storyline 
print(f"{ai}\n")
sprint("All the Henchmen have been dealt with in your apartment.\n")
sprint(f"'{player.name}, you have proven me wrong, I must say.'\n")
sprint("'No one has ever defeated a squadron of Henchmen alone...'\n")
sprint("'I now see why you were chosen for this mission.'\n")
sprint("Hahahahaha!\n")
sprint("'As much as I wish to congratulate you any longer, you still have a wo"
       "rld to save!'\n")
sprint("'You must now continue on with the mission.\n")
sprint("'Head to the location Morpheus sent you before and choose your car.'\n")
sprint("Good job for now...\n")

# Getting your Car
input("Press ENTER to go to Car Location :  \n\n")
sprint("Time : 2:35pm ")
sprint("Location : 9291 Burton Way, Beverly Hills \n")

input("Press ENTER to view your Car Options : \n")

# Creating The Blueprint for the Cars
# Using COMPOSITION


# Description of different cars
Car1 = Car(make = "BMW", model = "M5 Cs F90", engine = "S63 4.4-liter M TwinPower turbo V8", horse_power=627, wheel_size=21, tyre="Bridgestone")
Car2 = Car(make = "Mercedes", model = "C63 AMG W204", engine = "M156 6.2-liter V8", horse_power=450, wheel_size=18, tyre="Michelin")
Car3 = Car(make = "Porsche", model = "911 GT3 RS 997", engine = "4-litre Boxer 6-cylinder", horse_power=493, wheel_size=19, tyre="Michelin Pilot Sport Cup")
Car4 = Car(make = "Nissan", model = " GT-R R35", engine = "VR38 3.8-liter twin-turbocharged V6", horse_power=530, wheel_size=20, tyre="Michelin")

sprint("1." + Car1.display_car() +"\n")
sprint("2." + Car2.display_car() +"\n")
sprint("3." + Car3.display_car() + "\n")
sprint("4." + Car4.display_car() + "\n")

print(f"{ai}\n")
sprint("Choose Your Car Wisely :\n")
Move7 = input("[A] BMW M5 CS F90 \n[B] Mercedes C63 AMG W204 \n[c] Porsche 911 GT3 RS 997 \n[D] Nissan GT-R R35 \n\n").lower()
if Move7 == 'a':
    player.car = Car1
    sprint("What a Bavarian Beast!")
    sprint(f"You have Great Taste {player.name}\n")

elif Move7 == 'b':
    player.car = Car2
    sprint("Cant Go wrong With a C63 ... Right? ...\n")
    sprint("Try not to Spin out \n")
    
elif Move7 == 'c':
    player.car = Car3
    sprint("Ahh, the Porsche 911 GT3 RS. A true track weapon!\n")
    sprint(f"Excellent choice, {player.name}! It's built for speed and precision.\n")

elif Move7 == 'd':
    player.car = Car4
    sprint("Nissan GT-R R35 Godzilla on wheels!")
    sprint(f"You've chosen raw power, {player.name}. This will help you make a quick escape.\n")

else:
    print("Invalid choice. Please select a car from the options.\n")
    Move7 = input("[A] BMW M5 CS F90 \n[B] Mercedes C63 AMG W204 \n[c] Porsche 911 GT3 RS 997 \n[D] Nissan GT-R R35 \n\n").lower()

input("Press ENTER to get in your car and continue the mission.\n")
sprint("Time: 2:45 pm")
sprint("Location: On route to 12th Ave, Santa Cruz\n")
player.car.drive(10)

# The Cars
print(f"{ai}\n")
sprint(f"You're now driving the {player.car.model}.")
sprint("You are 349 miles away from The Matrix Base\n")
sprint(f"'{player.name} watch out there are some Matrix Agents in sedans in the Area'\n")

# The BMW
if player.car == Car1:
    # BMW M5 CS F90 Scenario
    sprint("Time: 3:00 pm")
    sprint("Location: The Highway\n")
    sprint("Your now Entering The highway ..., Everything seems fine ...\n")
    sprint(" As soon as you hit the highway, Two dark sedans from the Matrix agents start tailing you. You punch the gas, and the 627 BHP roars to life.")
    sprint("The Matrix agents are struggling to keep up, but they are closing in. \n")

    sprint(" Do you : \n")
    Move = input("[A] Floor it and try to outpace them?\n[B] Get off the Highway into Backstreets at the next exit and then Try to lose them?\n").lower()

    if Move == 'a':
        sprint("Time: 3:20 pm")
        sprint("Location: On route to 12th Ave, Santa Cruz\n")
        sprint("You hit 190mph and leave the agents in the dust. The M5 raw power gives you the edge!\n")
        sprint("Its going to be one nice long road down to California\n")
        player.car.drive(300)

    else:
        sprint("You get off the Highway, turn into the backstreets, and thanks to the M5 handling, you swiftly lose one of the Sedans in the maze of alleys.")
        player.car.drive(30)
        sprint("You are feeling Hungry and there is a Supermarket Right Next to you, However you know that time is the essence.\n")

        sprint("Do you : \n")
        Move = input("[A] Go into the Supermarket And Re-Energize?\n[B] Head Back onto the Highway to head to Location?\n").lower()

        if Move == 'a':
            sprint("I guess someone is Hungry\n")
            input("Press ENTER to go inside the supermarket\n")
            player.visit_supermarket()
            sprint(f"{player.name} Now that you are Re-Energized, You now need to continue on with your Journey Quickly, However you have 2 route options\n")

            sprint("Do You:")
            Move =  input("[A] Head Back onto the Highway?\n[B] Take the Backroads\n").lower()

            if Move == 'a':
                sprint(f"Pretty Good Decision {player.name}")
                sprint("Time: 3:40 pm")
                sprint("Location: The Highway\n")
                sprint("Its going to be one nice long road down to California\n")
                player.car.drive(240)

            elif Move == 'b':
                sprint("I Guess you just love Twist And Turns\n")
                sprint("Time: 3:40 pm")
                sprint("Location: Backroads\n")
                sprint("This is going To be a long trip to California\n")
                sprint("Your Fuel is going to take a massive hit for sure\n")
                player.car.drive(330)

        elif Move == 'b':
            sprint("The Matrix Agents in sedans Were both waiting for you at the Highway Entrance\n")
            sprint("You Should have Waited Abit Longer\n")
            sprint("Mission Failed.")
            exit()

    # The Mercedes
elif player.car == Car2:
    # Mercedes C63 AMG W204 Scenario
    sprint("Time: 3:00 pm")
    sprint("Location: Country Roads\n")
    sprint("You are now entering country roads\n")
    sprint("You are speeding down a narrow country road when a thunderstorm hits, making the road slippery.")
    sprint("The raw power of your V8 is a bit much for the slick roads, and you feel the rear end starting to slip.")
    print("Do you:")
    decision = input("[A] Ease off the throttle and regain control?\n[B] Continue fast around the corners drifting as you know that time is the essence\n").lower()
    if decision == 'a':
        sprint("Time: 3:20 pm")
        sprint("Location: Country Roads\n")
        sprint("You slow down and regain traction, carefully navigating through the storm. Smart move!\n")
        player.car.drive(200)
        sprint("You have been Driving through the country roads for some time now ... , You look through your rear mirrors and see a Dark sedan\n")
        sprint("You instantly detect the sedan as the Matrix Agents Sedan\n")
        sprint("You now need to Lose the Matrix Agent as the sedan begins picking up speed towards you")
        sprint("You know that the Power of your car can easily lose the Sedan on the country roads.\n However there is also an exit coming up leading to the Highway.\n")

        print("Do you:")
        Move = input("[A] Put your Foot down and try to lose the sedan on the country roads?\n[B] Exit onto the Highway and try to lose the sedan there?\n").lower()

        if Move == 'a':
            sprint("Time: 5:00 pm")
            sprint("Location: Unkown\n")
            print(f"{player.name}:\n")
            sprint("'OH NO F*Ck!'\n")
            print(f"{ai}\n")
            sprint(f"{player.name} you were moving at 160mph on the country roads, Whilst the roads were still slippery\n")
            sprint("Therefore when you came to a harsh turn the C63 Could not cope and slided out; Causing you to Crash into a field\n")
            sprint("You wake up later, captured by the Matrix Agents\n")
            sprint("Mission Failed.")
            exit()

        elif Move == 'b':
            sprint("Time: 5:20 pm")
            sprint("Location: Unknown\n")
            print(f"{ai}\n")
            sprint(f"Wise Decision {player.name}\n")
            sprint("You Successfully exited onto the Highway with the Sedan still behind you but abit further\n")
            sprint("The power of your car then allowed you to easily gap the Sedan by miles, And then continue to California down the Highway\n")
            player.car.drive(130)
    else:
        sprint("Time: 3:35 pm")
        sprint("Location: Country Roads\n")
        sprint("You decide to drift, but the road is too slick!.\n you were moving at 160mph on the country roads You spin out at a harsh turn into some Fields.\n")
        sprint("You wake up later, captured by Matrix Agents\n")
        sprint("Mission Failed.")
        exit()

    # The Porsche
elif player.car == Car3:
    # Porsche 911 GT3 RS Scenario
    sprint("Time: 3:00 pm")
    sprint("Location: Downtown, Los Angeles\n")
    sprint("You are still driving in Los Angeles")
    sprint("The city streets are narrow and winding, perfect for the Porsche 911 GT3 RS, Therefore you are moving at a great speed.\n")
    sprint("You come to a red light and check your mirrors..\n")
    sprint("Suddenly you see 2 Black Drones behind you, You instantly realise that you are being pursued by Matrix drones.\n")
    sprint("It just got Worse as the Drones are Equipped with Mini Machine Guns!\n")
    sprint("These Drones are here for the Kill, And you need to escape them fast!\n")
    sprint("You hear the whirring of the drones above as you take sharp corners at full speed.")

    print("Do you:\n")
    Move = input("[A] Head towards the highway so that you can try and outpace them ?\n[B] Stay in the city and look for a Hidden place to wait for abit?\n").lower()

    if Move == 'a':
        sprint("Time: 3:30 pm")
        sprint("Location: The Highway\n")
        sprint("You head towards the highway and press your foot down, But the drones lock onto you with ease in the open. They are closing in fast!\n")
        sprint("The Drones got close enough and Sprayed down your car with the machine guns totally demolishing the tyres.\n")
        sprint("This caused you to spin out at a high speed on the Highway...\n")
        sprint("You Fatally Crashed and Died as the Engine Blew.\n")
        print(f"{ai}\n")
        sprint("'I guess you should Never underestimate Drones'\n")
        sprint("Mission Failed.")
        exit()

    else:
        sprint("Time: 3:15 pm")
        sprint("Location: Downtown, Los Angeles\n")
        sprint("You stay in the tight city streets.\n using the Porsche's agility to your advantage, You are able to lose the drones and find a underground car park of a Supermarket.\n")
        player.car.drive(30)
        sprint("You have Waited in the Underground car park for abit \n")
        sprint("You are feeling abit unenergized\n")
        sprint("It is now the right time to leave the Car park and Resume with your journey\n")

        print("Do you:")
        Move = input("[A] Go to the supermarket and Re-Energize?\n[B] Resume With your Journey?\n").lower()

        if Move == 'a':
            sprint("Well If you Must\n")
            input("Press ENTER to go inside the supermarket\n")
            player.visit_supermarket()
            sprint(f"{player.name} Now you are Re-Energized, You now need to continue on fast with your Journey Quickly\n")
            input("Press ENTER to continue with your journey\n")
            sprint("Time : 3:25pm ")
            sprint("Location : The Highway\n")
            sprint("Your now on the Highway on route to the Matrix Base")
            sprint("Just one Long Road Down to California ....\n")
            player.car.drive(340)

        elif Move == 'b':
            sprint("Very Well..\n")
            sprint("Time : 3:10pm ")
            sprint("Location : The Highway\n")
            sprint("Your now on the Highway on route to the Matrix Base")
            sprint("Just one Long Road Down to California ....\n")
            player.car.drive(340)

# The Nissan
elif player.car == Car4:
    # Nissan GT-R R35 Scenario
    sprint("Time: 3:00 pm")
    sprint("Location: Downtown, Los Angeles\n")
    sprint("You are still driving in Los Angeles\n")
    sprint("You are Making your way towards the Highway and out of the City.\n")
    sprint("Now you are at a red light, When all of a Sudden you can hear a loud Buzzing sound.\n")
    sprint("You check your mirrors and then you look outside of your car ...\n")
    print(f"{player.name}:\n")
    sprint("'Oh No What The F*CK'\n")
    print(f"{ai}\n")
    sprint("To your Shock, You have just spotted a Dark Helicopter with Machine Guns.\n")
    sprint("You instantly Realise that the Helicopter was sent by the Matrix to Finish you off\n")
    sprint("You Now have to act fast before you are completely destroyed by the Machine Guns.\n ")
    sprint("The Nissan GT-Rs launch control catapults you forward as the helicopter locks onto your position.")
    sprint("You can try and outrun the Helicopter on the Highway.\n However you could also lose the Helicopter in the city and look for somewehere to hide for abit.\n")

    print("Do you:\n")
    Move = input("[A] Enter the Highway and then try to outrun the Helicopter on the Highway?\n[B] Try and lose the Helicopter on the city streets and Find a place to hide for abit?\n").lower()

    if Move == 'a':
      sprint("Time: 3:30 pm")
      sprint("Location: Los Angeles, Near the Highway\n")
      sprint("You head towards the highway and press your foot down, But the Helicopter locks onto you with ease in the open!\n")
      sprint("The Helicopter got close enough and sprayed down your car with the machine guns totally demolishing your tyres.\n")
      sprint("This caused you to spin out at a high speed on the Highway...\n")
      sprint("You Fatally Crashed and Died as the Engine Blew.\n")
      print(f"{ai}\n")
      sprint("'I guess you should Never underestimate A Helicopter with Machine Guns'\n")
      sprint("Mission Failed.")
      exit()

    else:
       sprint("Time: 3:15 pm")
       sprint("Location: Downtown, Los Angeles\n")
       sprint("You stay in the tight city streets.\n using the GTRs Beauty of Drifting corners smoothly, You are able to lose the Helicopter Eventually and find a underground car park of a Supermarket.\n")
       player.car.drive(30)
       sprint("You have now Waited in the Underground car park for abit \n")
       sprint("You are feeling abit unenergized\n")
       sprint("It is now the right time to leave the Car park and Resume with your journey\n")

       print("Do you:\n")
       Move = input("[A] Go to the supermarket and Re-Energize?\n[B] Resume With your Journey?\n").lower()

       if Move == 'a':
           sprint("Well If you Must\n")
           input("Press ENTER to go inside the supermarket\n")
           player.visit_supermarket()
           sprint(f"{player.name} Now you are Re-Energized, You now need to continue on with your Journey Quickly\n")
           input("Press ENTER to continue with your journey\n")
           sprint("Time : 3:25pm ")
           sprint("Location : The Highway\n")
           sprint("Your now on the Highway on route to the Matrix Base")
           sprint("Just one Long Road Down to California ....\n")
           player.car.drive(320)

       elif Move == 'b':
           sprint("Very Well..\n")
           sprint("Time : 3:10pm ")
           sprint("Location : The Highway\n")
           sprint("Your now on the Highway on route to the Matrix Base")
           sprint("Just one Long Road Down to California ....\n")
           player.car.drive(320)

# End of Car Scenarios And options
     
# The Infiltration
input("Press ENTER to continue on ...\n")
print("Mission continues...\n")

# Approaching the Matrix Base
sprint("Time: 7:45 PM")
sprint("Location: California, 9th Ave, Santa Cruz \n")
print(f"{ai}\n")
sprint("Quite the journey, wasn't it?\n")
sprint(f"After all the chaos, {player.name}, you've finally made it to California.\n")
sprint("Congratulations on getting here in one piece.\n")
sprint("Hahaha!\n")
sprint("Well, well...\n")
sprint("This is where things start to get serious.")
sprint("Remember, your mission is simple but critical: infiltrate the Matrix base and retrieve the files before they are wiped out.")
sprint("It all comes down to this...\n")
sprint("Tonight, the fate of the world is in your hands.\n")
sprint("No pressure, of course.\n")
sprint(f"Alright, {player.name}, it's time.\n")
sprint("You'll need to stash your car somewhere safe before we proceed.\n")
sprint("Choose where you want to stash your car \n")
print("Do you : \n")

Move = input("[A] Stash your car in the Underground Car Park of Walmart ? \n[B] Stash your car behind Target ? \n").lower()

if Move == 'a':
    print(f"{ai}\n")
    sprint("'Very Well.'\n")

    if player.HP <= 50:
        sprint(f"{player.name} your Health is Very low.\n")
        sprint("You should Visit Walmart and Re-Energize before going into the Matrix Base.\n")
        input("Press ENTER to go inside Walmart \n")
        player.visit_supermarket()
        sprint("Feeling better already. Now, let's get to work.\n")
    sprint(f"{player.name}, it's game time.\n")
    input("Press ENTER to continue")

elif Move == 'b':
    print(f"{ai}\n")
    sprint("'Ahhhh Cheeky Boy'\n")

    if player.HP <= 80:
        sprint(f"{player.name} your Health is Very low.\n")
        sprint("You should Visit Target and Re-Energize before going into the Matrix Base.\n")
        input("Press ENTER to go inside Target")
        player.visit_supermarket()
        sprint("Now thats Better!\n")
    sprint(f"{player.name} its Gametime now.\n")
    input("Press ENTER to continue")

    # Approaching the Matrix Base
sprint("Time: 8:45 PM")
sprint("Location: The Matrix Base, 13th Ave, Santa Cruz \n")
sprint("You Have arrived outside the matrix Base.\n")
sprint("Hiding Behind a Tree.\n")
sprint(f"Alright, {player.name}, your first objective is to get inside the Matrix base compound.\n")
sprint("The main entrance is a no-go; security's way too tight.\n")
sprint("You'll have to find another way in and quietly.\n")
sprint("Infiltrate the compound carefully, avoid detection at all costs.\n")
sprint("The clock's ticking. Make your move. \n")

# Provide the player with options for approaching the base
sprint("Do you: \n")
Move = input("[A] Climb The Fence into the Compound? \n[B] Enter through the Back Entrance Using Stealth?\n").lower()

if Move == 'a':
    # Fence Approach
    sprint("You begin climbing the Fence behind the Container.\n")
    sprint("You find yourself in a situation as you get to the top of the Fence.\n")
    sprint("The fence is lined with sharp spikes, something you had not noticed before.\n")
    sprint("There is no turning back now!\n")

    print("Do you:\n")
    Move = input("[A] Try to hurdle over the spikes?\n[B] Look for a way to cover the spikes?\n").lower()

    if Move == 'a':
        # Option to hurdle over the spikes
        sprint("You brace yourself and prepare to leap over the spikes.\n")
        sprint("With a burst of energy, you jump, trying to clear the sharp points...\n")
        hurdle_success = random.choice([True, False])  # Random chance for success
        
        if hurdle_success:
            sprint("You manage to Successfully Hurdle over the spikes.\n")
            print(f"'{player.name} you Really avoided those spikes like a Ninja'")
            sprint("You can see a entrance into the Building.\n")
            input("Press ENTER to go to the entrance \n")
            sprint("You are now at the entrance, And to your suprise there are no Matrix Guards to be seen.\n")
            input("Press ENTER to go inside the Matrix Base \n")

        else:
            sprint("You leap, but your leg catches one of the spikes!\n")
            sprint("You manage to pull yourself over, but you are bleeding from a nasty cut.\n")
            player.HP -= 20  # Reduce player's health
            sprint(f"{player.name}, you lose 20 HP. Current HP: {player.HP}\n")
            sprint("You have to patch up the Wound.\n")
            input("Press ENTER to patch up wound \n")
            player.HP -= 20  # Give Back Health
            sprint("You Found some Cloth in the Container and used it to patch up your wound.\n")
            sprint("Your leg will be fine for now.\n")
            sprint("You can see a entrance into the Building.\n")
            input("Press ENTER to go to the entrance \n")
            sprint("You are now at the entrance, And to your suprise there are no Matrix Guards to be seen.\n")
            input("Press ENTER to go inside the Matrix Base \n")

    elif Move == 'b':
        # Option cover the spikes
        sprint("You carefully look around the top of the fence for something to help.\n")
        sprint("To your luck you spot a little branch from the tree, You grab the Little Branch.\n")
        sprint("It is not perfect, but it should work and prevent anything from happening.\n")
        sprint("You climb over using the Branch as cover, avoiding the sharp points, and you make it to the other side safely!\n")
        print(f"{ai}\n")
        sprint("'Good thinking! You avoided injury.'\n")
        sprint("You can see a entrance into the Building.\n")
        input("Press ENTER to go to the entrance \n")
        sprint("You are now at the entrance, And to your suprise there are no Matrix Guards to be seen.\n")
        input("Press ENTER to go inside the Matrix Base \n")

elif Move == 'b':
    # Stealth Approach
    sprint("You decide to sneak towards the back entrance.\n")
    sprint("Keeping low to the ground, you move silently in the shadows.\n")
    sprint("As you get closer, you spot a Matrix Guard near the entrance.\n")
    sprint("You will need to Deal with the Matrix Guard to Enter the Building.\n")

    print("Do you :\n")
    Move = input("[A] Distract the Matrix Guard?\n[B] Wait for the Matrix Guard to turn away, Then take him out quickly?\n").lower()

    if Move == 'a':
        sprint("You Find some Pebbles on the ground, You then use the Pebbles to distact the guard by throwing them.\n")
        sprint("You swiftly Begin Moving to the Entrance.\n")
        Entrance_success = random.choice([True, False])  # Random chance for success

        if Entrance_success:
            sprint("Luckily, You make it to the Entrance without getting caught.\n")
            input("Press ENTER to go inside the Matrix Base")
            sprint("You slip through the entrance unnoticed. Good work!\n")

        else:
            sprint("The Matrix Guard Heard one of your footsteps as you were moving.\n")
            print(f"{mg}\n")
            sprint("'WHO ARE YOU!'\n")
            print(f"{ai}\n")
            sprint("The Matrix Guard is approaching you.\n")
            sprint("Your back is faced towards him.\n")
            sprint("The Matrix Guard is Right Behind you now and is pointing a Gun at you.\n")

            print("Do you : \n")
            Move = input("[A] Turn and Knock Out the Henchman using your Fists?\n[B] Turn and Reach for your Weapon to take him out?\n")

            if Move == 'a':
               sprint(f"{player.name} you turn around smoothly and give the Matrix Guard a punch right on the nose.\n")
               sprint("The Matrix Guard was Instantly Knocked out Clean!\n")
               print(f"{ai}\n")
               sprint("What a Hit, I am Certainly Impressed. \n")
               sprint(f"{player.name} you must quickly tie up this body, Then head into the Base. \n")
               input("Press ENTER to tie up the Matrix Guards Body \n")
               sprint("The Matrix Guards body has been dealt with.\n")
               input("Press ENTER to go inside the Matrix Base \n")

            elif Move == 'b':
                sprint("You Turned Around Smoothly, However as you reached for your weapon.\n")
                sprint("The Matrix Guard fired right away, This instantly knocked you out cold.\n")
                sprint("Later you woke up surrounded by Matrix Agents, Captured.")
                sprint(f"'{player.name} you were so close! \n")
                sprint("Mission Failed.")
                exit()
      
# Inside The Matrix Base - Finding the Files Room
print(f"{ai}\n")
sprint(f"You are now inside of the Matrix Base {player.name}.")
sprint("All, You need to do now is find the Files room")
sprint("There is a staircase infront of you which goes Upstairs and Downstairs.\n")

print("Do you: \n")
Move = input("[A] Take the Staircase Upstairs?\n[B] Take the Staircase Downstairs?\n").lower()

if Move == 'a':
    sprint("You take the staircase Upstairs.")
    sprint("However, there is a Matrix Guard.")
    print(f"{player.name} you can use this as a opportunity to find out where the Files room is.\n")

    print("Do you :\n")
    Move = input("[A] Sneak up behind and point your weapon to his head?\n[B] Stay Hidden for abit and watch the guard?\n").lower()

    if Move == 'a':
        sprint("You sneak up to the guard from behind, moving as silently as possible.\n")
        sprint("You press your weapon to the back of his head and speak in a low voice.\n")
        print(f"{player.name}:\n")
        sprint("'Where is the files room?' \n")
        sprint("'You have 5 seconds to tell me or your dead!'\n")
        print(f"{mg}\n")
        sprint("'Please dont shoot me!' \n")
        sprint("'If you want to go to the files room, Go Downstairs '\n")
        sprint("'then take a right and go down to the end of the corridor!' \n")
        sprint("'Now Please let me GO'\n")
        print(f"{player.name}:\n")
        sprint("'Not just Yet'\n")
        input("Press ENTER to hit the Matrix Guard and make him unconscious. \n")
        sprint("The Matrix Guard is now unconscious. \n")
        input("Press ENTER to Hide the Matrix Guard. \n")
        sprint("The Matrix Guard is now hidden.\n")
        print(f"{ai}\n")
        sprint("'Good Work there.'\n")
        sprint("'You now know where to find the files room'\n")
        sprint("'You must hurry and get there, Before the Matrix guard wakes up and the whole place is alerted!'\n")
        sprint("Press ENTER to go Downstairs\n")
        sprint("You are now Downstairs \n")

    elif Move == 'b':
        sprint("You decide to stay hidden and observe the guard for a moment.\n")
        sprint("The Matrix guard is now talking into his earpiece.\n")
        print(f"{mg}\n")
        sprint("'Boss said im switching with you in 20 mins to guard the files room...'\n")
        sprint("'I've never actually guarded the files rooom before ...'\n")
        sprint("'All i know is that its all the way downstairs and on the right'\n")
        sprint("'Alright yes, I will be there in 30 mins'\n")
        print(f"{ai}\n")
        sprint(f"'{player.name}, I think today is your lucky day.'\n")
        sprint("You hear the Matrix Guard mention something about a security shift change and the location of the Files room.\n")
        sprint("It looks like your patience paid off.\n")
        sprint("'You now know where to find the files room'\n")
        sprint("'You must hurry and get there'\n")
        sprint("Press ENTER to go Downstairs \n")
        sprint("You are now Downstairs\n")

elif Move == 'b':
    # Player takes the staircase downstairs
    sprint("You decide to take the staircase downstairs.\n")
    sprint(f"{player.name}, you hear faint footsteps approaching from around the corner.\n")
    sprint("You peek your head and see that there is a Matrix guard.\n")
    print(f"{player.name} you can use this as a opportunity to find out where the Files room is. \n")

    print("Do you :\n")
    Move = input("[A] Sneak up behind and point your weapon to his head?\n[B] Stay Hidden for abit and watch the guard?\n").lower()

    if Move == 'a':
        sprint("You sneak up to the guard from behind, moving as silently as possible.\n")
        sprint("You press your weapon to the back of his head and speak in a low voice.\n")
        print(f"{player.name}:\n")
        sprint("'Where is the files room?' \n")
        sprint("'You have 5 seconds to tell me or your dead!'\n")
        print(f"{mg}\n")
        sprint("'Please dont shoot me!' \n")
        sprint("'The files room is on the right at the end of this corridor! '\n")
        sprint("'Now Please let me GO'\n")
        print(f"{player.name}:\n")
        sprint("'Not just Yet'\n")
        input("Press ENTER to hit the Matrix Guard and make him unconscious. \n")
        sprint("The Matrix Guard is now unconscious. \n")
        input("Press ENTER to Hide the Matrix Guard. \n")
        sprint("The Matrix Guard is now hidden.\n")
        print(f"{ai}\n")
        sprint("'Good Work there.'\n")
        sprint("'You now know where to find the files room'\n")
        sprint("'Go to the files room, Before the Matrix guard wakes up and the whole place is alerted!'\n")
    
    elif Move == 'b':
        sprint("You decide to stay hidden and observe the guard for a moment.\n")
        sprint("The Matrix guard is now talking into his earpiece.\n")
        print(f"{mg}\n")
        sprint("'Boss said im switching with you in 20 mins to guard the...'\n")
        sprint("'Thats Alright, I can tell you where it is ...'\n")
        sprint("'The files room is here, Downstairs and on the right at the end of the corridor'\n")
        sprint("'No Problem.\n'\n")
        print(f"{ai}\n")
        sprint(f"'{player.name}, I think today is your lucky day.'")
        sprint("You hear the Matrix Guard mention something about a security shift change and the location of the Files room.\n")
        sprint("It looks like your patience paid off.\n")
        sprint("'You now know where to find the files room'\n")
        sprint("'Hurry and get to the files room'\n")
        
# Gettng inside the files room

input("Press ENTER to go to the files room. \n")
sprint(f"{player.name}, you are now infront of the files room, However you cannot get inside without a code.\n")
sprint("This should not be a problem as you are a hacker, One of the Best Hackers in the World! \n")
print(f"{ai}\n")
sprint(f"{player.name}, You must quickly Bypass the door and get inside.\n")

# Hacking Mini Game
input("Press ENTER to hack the door.\n")
hack_door

if hack_door():
    sprint("You successfully hacked the door and gained access!\n")
    sprint("The scanner lights turn green. The door hisses open.\n")
    input("Press ENTER to go inside the File Room \n")
    print(f"{ai}\n")
    sprint("'You truly are one of the best.'\n")
else:
    sprint("You failed to hack the door. Security is alerted! \n")
    print(f"{ai} \n")
    sprint(f"'Disapponting.'\n")
    sprint("Mission Failed.\n")
    exit()

sprint(f"{player.name}, You are nearly there, The fate of the world might just be in good hands after all! \n")
sprint("Now quick, you must find the stick With the Data and Leave! \n")

print("Do you: \n")
Move = input("[A] Search The Computer Desk for the Stick?\n[B] Search the Lockers for the Stick?\n").lower()

# Searching the Computer
if Move == 'a':
    sprint("You Search everywhere on the Computer desk for the drive, However it is not visible \n")

    print("Do you: \n")
    Move = input("[A] Search the Lockers for the Stick?\n[B] Look around the room Hoping to Find it?\n").lower()

    if Move == 'a':
        sprint("You look in the lockers, But the stick is still not visible. \n")
        sprint("All you can really do now is look around the room and hope for the best. \n")
        sprint("Time is really Running out ... \n")
        input("Press ENTER to look around the room \n")
        sprint("you are looking around desperately now, When ... \n")
        sprint("CLICK ... \n")
        sprint("You Stepped on a button which triggered a Hidden door.\n")
        sprint("On the other side of the Door is a Vault. \n")


    elif Move == 'b':
        sprint("you are looking around desperately now, When ... \n")
        sprint("CLICK ... \n")
        sprint("You Stepped on a button which triggered a Hidden door.\n")
        sprint("On the other side of the Door is a Vault. \n")

    else:
        sprint("Invalid Output!\n")
        Move = input("[A] Search the Lockers for the Stick?\n[B] Look around the room Hoping to Find it?\n").lower()

# Searching the Computer
elif Move == 'b':
    sprint("You look in the lockers, But the stick is still not visible. \n")

    print("Do you: \n")
    Move = input("[A] Search The Computer Desk for the Stick?\n[B] Look around the room Hoping to Find it?\n").lower()

    if Move == 'a':
         sprint("You Search everywhere on the Computer desk for the drive, However the stick is still not visiible.\n")
         sprint("All you can really do now is look around the room and hope for the best. \n")
         sprint("Time is really Running out ... \n")
         input("Press ENTER to look around the room \n")
         sprint("you are looking around desperately now, When ... \n")
         sprint("CLICK ... \n")
         sprint("You Stepped on a button which triggered a Hidden door.\n")
         sprint("On the other side of the Door is a Vault. \n")

    elif Move == 'b':
        sprint("you are looking around desperately now, When ... \n")
        sprint("CLICK ... \n")
        sprint("You Stepped on a button which triggered a Hidden door.\n")
        sprint("On the other side of the Door is a Vault. \n")

    else:
        sprint("Invalid Output!\n")
        Move = input("[A] Search The Computer Desk for the Stick?\n[B] Look around the room Hoping to Find it?\n").lower()


# Getting into the Vault to get the Stick
print(f"{ai}\n")
sprint("'Of Course they put the stick in a Vault!' \n")
sprint(f"'{player.name} i guess you are going to need to use your hacking skills again.'\n")
sprint("Hack the pin of the Vault and retrieve the Stick.\n")
sprint("Hurry, You dont have much time left now.\n")

input("Press ENTER to go to the Vault. \n")
sprint("You are now infront of the vault.\n")
input("Press ENTER to hack into the Vault.\n")

# Second Hacking Game
hack_vault

if hack_vault():
    sprint("You successfully hacked the Vault and gained access!\n")
    sprint("The Vault Door Slowly Opens\n")
    input("Press ENTER to go inside the Vault.\n")
    print(f"{ai}\n")
    sprint("'Wow. That was easy for you.'\n")
else:
    sprint("You failed to hack the vault. The stick was not retrieved. Building was alerted!\n")
    print(f"{ai} \n")
    sprint(f"'All for Nothing.'\n")
    sprint("Mission Failed.\n")
    exit()

# Getting the Stick Then Leaving.
sprint(f"Good Job {player.name}, Now Find the Stick \n")
input("Press ENTER to look in the vault for stick.\n")

sprint("You look around the vault for the stick, But there is just a Load of files and duffle bags.\n")
sprint("You are about to give up, But you come to the end of the vault and see a Stand with the Stick displayed on it.\n")
sprint("At Last!, you have found the Stick.\n")

input("Press ENTER to Get the Stick. \n")
sprint(f"As you grab the Stick, an alarm suddenly blares throughout the building!\n")
sprint("Red lights start flashing, and a loud siren echoes through the vault.\n")

print(f"{ai}\n")
sprint(f"'Oh no, {player.name}! You've triggered an alarm! You need to get out of there fast!'\n")
sprint("'You have come this far, You must Escape from the Matrix Base and Get to your car'\n")

input("Press ENTER to leave the vault and the File room.")
sprint("You have left the vault and the File room.")
input("Press ENTER to run down the corridor to the staircase")
sprint("You are now at the Staircase.\n")
input("press ENTER to run upstairs to the exit.\n")
sprint("You are now at the exit.\n")
print(f"{mg}\n")
sprint(''"I FOUND THE INTRUDER!'\n")
sprint("'IM TAKING HIM DOWN AT ENTRANCE F1.' \n")

# Matrix Guard Quick Battle
print(f"{ai}\n")
sprint("A Matrix Guard is blocking your exit, And is rushing towards you.\n")
sprint("Everyone will be coming after you, You must take him down quickly and"
       "run!\n")

sprint("Press ENTER to Fight. \n")
battle()

print(f"{ai}\n")
sprint(f"'{player.name}, Good Job.'\n")
sprint("However no time to stop, You must get out of the compound immediately!\n")
sprint("Unfortunately, you will have to exit through the back entrance.\n")

input("Press ENTER to run to Back entrance. \n")




