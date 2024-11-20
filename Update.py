#####################################################
## THE MATRIX PROJECT - TEXT BASED ADVENTURE GAME  ##
#####################################################

# Importing all the modules to operate THE MATRIX
import random

from cc import *
from Cars import *   
from Hg import *
from cs import*
from Mb import *
from Bttle import *


start=True  # Allowing the exit function to work 


# Asking the player if they want to play the game
answer = input("Would You like to Take on the Matrix: yes or no \n").lower()
if answer == "yes":
    sprint("Game Loading.... Game Loading.... Game Loading.... Game Loading..."
           ".\n")

elif answer == "No":
    sprint("Maybe Next time")
    exit()

else:
    print("Please enter yes or no.")
    answer = input("Would You like to Take on the Matrix: Yes or No \n")



print(f"{ai}\n")
sprint(f"{player.name}, You are an Elite Hacker and a key member of the"
       " organization The Real World.\n")
sprint("For the past few years you have been working to end the"
      " tyranny of The Matrix and" 
       " Their evil plans to take control over the world.\n") 
sprint("The Real World have finally gathered enough data to finally end the"
      " corruption of The Matrix. However just today ...\n")

enter()

sprint("Time : 11:00am ")
sprint("Location : 9291 Burton Way, Beverly Hills\n")

# The Fisrt Speech
print(f"{npc}\n")
sprint(f"'Dear {player.name},'\n")
sprint("'By the time you are reading this message, The Matrix would have taken"
       " down The Real World and our Database.'\n")
sprint("'They have located our main headquarters, and this morning they "
       "launched a full-scale assault, destroying all our Resources.'\n")
sprint("'I was fortunate enough to escape their henchmen, but I am currently"
       " hiding in a safe house, keeping a low profile.'\n")
sprint("'However, The Matrix has become aware of our knowledge regarding their"
      " secrets and Dark Arts, and they are coming after every member of the"
      " Real World.'\n")
sprint("'The fate of the Real World and everything we have fought for now "
       "rests on your shoulders.'\n")
sprint(f"'I believe that you are the only one who possesses the skills to save"
      " us and execute our original mission.'\n")
sprint(f"'{player.name}, you must leave your apartment immediately after"
       " reading this.'\n")
sprint("'They will be at your door any second, and time is of the essence. I"
       " will provide you with the location to retrieve a car.'\n")
sprint("'You must Grab one of the Cars from the Location and Locate then head"
       " to the Matrix Headquarters and retrieve our files before they are"
      " destroyed.'\n")
sprint("'Once you Retrieve the files from The Matrix you can contact me through"
       " this network and i will tell you where to meet me'\n")
sprint("'Good luck; our fate hinges on your success.'\n")
sprint("'Remember, no pressure!'\n")

print(f"{npc}\n")
sprint("Car Location : 155 N Crescent Dr, Beverly Hills\n")

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

enter()

# Player Chooses Their Weapon
weapon = ""
print(f"{ai}\n")
sprint("'Here is your Weaponry Selection' \n")
print("Choose your Weapon Wisely : \n")

Wc()

# Getting to the Battle
print(f"{hmanb}\n")
sprint("'He's there Take him down!' \n")

print(f"{ai}\n")
sprint(f"One of the Matrix Henchmen is barreling toward you, ready to take you"
      " down!\n")
sprint(f"'{player.name} Will you Fight the Henchman or Surrender?'\n")

print(f"{ai}\n")
Move2 = input("[A] Proceed to Fight\n[B] Surrender \n\n").lower()

while True:
        if Move2 == 'a' :
            sprint("Good luck "+player.name+" \n")
            break
    
        elif Move2 == 'b':
            sprint("'You have perished and failed your mission.'")
            sprint("You will now be taken to the start \n")
            exit()

        else:
             print("Choose one! You can't escape your fate.")
             Move2 = input("[A] Proceed to Fight\n[B] Surrender \n\n").lower()


print(f"{ai}\n")
sprint(f"Your current Health is {player.HP}\n")
print(f"The Henchman's Health is {matrix_henchman[0].HP}\n")

print(f"{ai}\n")
print(f"Its time to Take on the Henchman",player.name,"! \n\n")
input("Press ENTER to continue to battle:  \n\n")
sprint("Proceeding into battle ...   Proceeding into battle ...   Proceeding"
      " into battle ...  Proceeding into battle ... \n")


sprint("\n" + "=" * 40)
sprint("  == THE MATRIX HENCHMAN BATTLE ==")
sprint("\n" + "=" * 40)

Fb()
enter() 

# Storyline
print(f"{hmanb}\n")
sprint("'Impossible How has he Defeated one of us ... !'\n")
sprint("'Finish Him off!!!'\n")

print(f"{ai}\n")
sprint("'You dealt with that Henchman like a true warrior!'\n")
sprint("'But unfortunately, you are nowhere near finished here.'\n")
sprint("'The Henchman Boss has just sent another one of his minions to"
       " challenge you!'\n")
input("Press ENTER to continue to the next battle:\n\n")

sprint(f"Your current Health is {player.HP}\n")
sprint(f"This Henchman's health is {matrix_henchman[1].HP}\n")

Sb()
enter()

# Storyline
print(f"{hmanb}\n")
sprint("'No! This can't be!'\n")
sprint("'Well then... I guess I will have to take matters into my own "
        "hands.'\n")
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
Lb()

print(f"{hmanb}\n")
sprint("'Oh No THIS CANNOT BE HAPPENING RIGHT NOW!'\n")
sprint("'The Matrix Will not let you get away with this !!!'\n\n")
print(f"{ai}\n")
sprint(f"'{player.name} You must Get The location of the Matrix Base By"
      " torturing this Henchman'\n")
enter()
print(f"{player.name}: \n")
sprint("'Tell me where The Matrix base is or I shall end you'\n")
print(f"{hmanb}\n")
sprint("'Never!\n")
print(f"{player.name}: \n")
sprint("'Fine,you choose Pain'\n")
print(f"{ai}\n")
sprint(f"Make your decision Wisely {player.name} :\n")
Move6 = input("[A] Get Henchman to talk by Waterboarding Him \n[B] Get"
              " Henchman to talk by Lighting him on Fire\n").lower()
while True:
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
             break

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
            Move6 = input("[A] Get Henchman to talk by Waterboarding Him \n[B] Get"
                          " Henchman to talk by Lighting him on Fire\n").lower()

# Storyline 
enter()
print(f"{ai}\n")
sprint("All the Henchmen have been dealt with in your apartment.\n")
sprint(f"'{player.name}, you have proven me wrong, I must say.'\n")
sprint("'No one has ever defeated a squadron of Henchmen alone...'\n")
sprint("'I now see why you were chosen for this mission.'\n")
sprint("Hahahahaha!\n")
sprint("'As much as I wish to congratulate you any longer, you still have a"
      " world to save!'\n")
sprint("'You must now continue on with the mission.\n")
sprint("'Head to the location Morpheus sent you before and choose your car."
       "'\n")
sprint("Good job for now...\n")

# Getting your Car
input("Press ENTER to go to Car Location:\n\n")
sprint("Time : 2:35pm ")
sprint("Location : 9291 Burton Way, Beverly Hills\n")

input("Press ENTER to view your Car Options.\n")

# Description of different cars
Car1 = Car(make = "BMW", model = "M5 Cs F90", engine = "S63 4.4-liter"
          " M TwinPower turbo V8", horse_power=627, wheel_size=21,
         tyre="Bridgestone")
Car2 = Car(make = "Mercedes", model = "C63 AMG W204", engine = "M156 6.2-liter"
          "V8", horse_power=450, wheel_size=18, tyre="Michelin")
Car3 = Car(make = "Porsche", model = "911 GT3 RS 997", engine = "4-litre "
           "Boxer 6-cylinder", horse_power=493, wheel_size=19,
          tyre="Michelin Pilot Sport Cup")
Car4 = Car(make = "Nissan", model = " GT-R R35", engine = "VR38 3.8-liter"
          " twin-turbocharged V6", horse_power=530,
         wheel_size=20, tyre="Michelin")

sprint("1." + Car1.display_car() +"\n")
sprint("2." + Car2.display_car() +"\n")
sprint("3." + Car3.display_car() + "\n")
sprint("4." + Car4.display_car() + "\n")

scenario()

# End of Car Scenarios And options
enter()
print("Mission continues...\n")

# Approaching the Matrix Base
sprint("Time: 7:45 PM")
sprint("Location: California, 9th Ave, Santa Cruz \n")
print(f"{ai}\n")
sprint("Quite the journey, wasn't it?\n")
sprint(f"After all the chaos, {player.name}, you've finally made it to"
       " California.\n")
sprint("Congratulations on getting here in one piece.\n")
sprint("Hahaha!\n")
sprint("Well, well...\n")
sprint("This is where things start to get serious.")
sprint("Remember, your mission is simple but critical: infiltrate the Matrix"
       " base and retrieve the files before they are wiped out.")
sprint("It all comes down to this...\n")
sprint("Tonight, the fate of the world is in your hands.\n")
sprint("No pressure, of course.\n")
sprint(f"Alright, {player.name}, it's time.\n")
sprint("You'll need to stash your car somewhere safe before we proceed.\n")
sprint("Choose where you want to stash your car.\n")
enter()

Move = input("[A] Stash your car in the Underground Car Park of Walmart ?\n"
             "[B] Stash your car behind Target ? \n").lower()

while True:
    if Move == 'a':
        print(f"{ai}\n")
        sprint("'Very Well.'\n")

        if player.HP <= 90:
            sprint(f"{player.name} your Health is Very low.\n")
            sprint("You should Visit Walmart and Re-Energize before going into"
                   " the Matrix Base.\n")
            input("Press ENTER to go inside Walmart \n")
            player.visit_supermarket()
            sprint("Feeling better already. Now, let's get to work.\n")
        sprint(f"{player.name}, it's game time.\n")
        break

    elif Move == 'b':
        print(f"{ai}\n")
        sprint("'Ahhhh Cheeky Boy'\n")

        if player.HP <= 80:
            sprint(f"{player.name} your Health is Very low.\n")
            sprint("You should Visit Target and Re-Energize before going"
                  " into the"
                   " Matrix Base.\n")
            input("Press ENTER to go inside Target")
            player.visit_supermarket()
            sprint("Now thats Better!\n")
        sprint(f"{player.name} its Gametime now.\n")
        break

    else:
        sprint("Invalid Choice, Choose a option!\n")
        input("[A] Stash your car in the Underground Car Park of Walmart ?\n"
             "[B] Stash your car behind Target ? \n").lower()

    # Approaching the Matrix Base
enter()
sprint("Time: 8:45 PM")
sprint("Location: The Matrix Base, 13th Ave, Santa Cruz \n")
sprint("You Have arrived outside the matrix Base.\n")
sprint("Hiding Behind a Tree.\n")
sprint(f"Alright, {player.name}, your first objective is to get inside the"
       " Matrix base compound.\n")
sprint("The main entrance is a no-go; security's way too tight.\n")
sprint("You'll have to find another way in and quietly.\n")
sprint("Infiltrate the compound carefully, avoid detection at all costs.\n")
sprint("The clock's ticking. Make your move.\n")

# Provide the player with options for approaching the base
Gettinin()

# Inside The Matrix Base - Finding the Files Room
print(f"{ai}\n")
sprint(f"You are now inside of the Matrix Base {player.name}.")
sprint("All, You need to do now is find the Files room")
sprint("There is a staircase infront of you which goes Upstairs and"
       " Downstairs.\n")

Infiltration()

# Hacking Mini Game
input("Press ENTER to hack the door.\n")
hacking_success = hack_door()

if hacking_success:
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

sprint(f"{player.name}, You are nearly there, The fate of the world might just"
      " be in good hands after all! \n")
sprint("Now quick, you must find the stick With the Data and Leave! \n")

enter()
DataStick()

# Second Hacking Game
hacking1_success = hack_vault()

if hacking1_success:
    sprint("You successfully hacked the Vault and gained access!\n")
    sprint("The Vault Door Slowly Opens\n")
    input("Press ENTER to go inside the Vault.\n")
    print(f"{ai}\n")
    sprint("'Wow. That was easy for you.'\n")
else:
    sprint("You failed to hack the vault. The stick was not retrieved. Building"
          " was alerted!\n")
    print(f"{ai} \n")
    sprint(f"'All for Nothing.'\n")
    sprint("Mission Failed.\n")
    exit()

# Getting the Stick Then Leaving.
sprint(f"Good Job {player.name}, Now Find the Stick \n")
input("Press ENTER to look in the vault for stick.\n")

sprint("You look around the vault for the stick, But there is just a Load of "
       "files and duffle bags.\n")
sprint("You are about to give up, But you come to the end of the vault and see"
      " a Stand with the Stick displayed on it.\n")
sprint("At Last!, you have found the Stick.\n")

input("Press ENTER to Get the Stick. \n")
sprint(f"As you grab the Stick, an alarm suddenly blares throughout the "
       "building!\n")
sprint("Red lights start flashing, and a loud siren echoes through the vault."
       "\n")

# Middle Scene
print(f"{ai}\n")
sprint(f"'Oh no, {player.name}! You've triggered an alarm! You need to get out"
      " of there fast!'\n")
sprint("'You have come this far, You must Escape from the Matrix Base and Get"
      " to your car'\n")

input("Press ENTER to leave the vault and the File room.\n")
sprint("You have left the vault and the File room.\n")
input("Press ENTER to run down the corridor to the staircase.\n")
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
       " run!\n")

input("Press ENTER to Fight.\n")

sprint(f"{player.name} your current health is {player.HP}\n")
sprint(f"The Matrix Guard current health is {matrix_guard.HP}\n")


sprint("\n== MATRIX GUARD BATTLE ==\n")
Gb()
enter()

# Next Sequence
print(f"{ai}\n")
sprint(f"'{player.name}, Good Job.'\n")
sprint("However no time to stop, You must get out of the compound immediately!"
       "\n")
sprint("Unfortunately, you will have to exit through the back entrance.\n")

input("Press ENTER to run to Back entrance.\n")
sprint("You are now at the Back entrance, Suprisingly there are absolutely no"
      " Matrix Guards or Henchman. \n")
sprint(f"This might be easier than i thought {player.name}, Now Quickly run"
       " out of .....\n")

print(f"{mea}\n")
sprint(f"'We have found {player.name} Agent Myth.'\n")
sprint("'What should we do with him?'\n")
sprint("'Okay we will take him down!'\n")
sprint("'Agents Take him down!'\n")

print(f"{ai}\n")
sprint("'This might just be the end'\n")
sprint("Of course they had to send Matrix Agents.\n")
sprint("The Matxrix Agents block your entrance.\n")
sprint(f"{player.name} it has to be said the Matrix Agents empower you.\n")
sprint("Defeating the Matrix Agents would be a true miracle.\n")
sprint("You cannot run away from them, unfortunately there is no escape "
       " here...\n")
sprint("You will have to fight the Matrix Agents.\n")
sprint("Good luck my Friend.\n")
input("Press ENTER to Battle with Matrix Agents.\n")

# Battle with 2 Agents
sprint(f"{player.name} your current health is {player.HP}.\n")

sprint("\n" + "=" * 40)
sprint("  == THE BATTLE OF MATRIX AGENTS ==")
sprint("\n" + "=" * 40)
Mab()
enter()

print(f"{ai}\n")
sprint("'I am genuinely lost for words.\n'")
print(f"{mea}\n")
sprint("'Agent Myth'\n")
sprint("'We have a big problem'\n")
sprint("'The guy is not normal.'\n")
sprint("'Forgive me if i fail.'\n")

sprint("The Last Matrix Agent pulls out a Matrix Rifle and starts spraying "
       "bullets in your direction.\n")
print(f"{player.name}, your health is currently {player.HP}.\n")


Mab2()
enter()

sprint(f"'{player.name} YOU HAVE JUST ACCOMPLISHED SOMETHING WHICH HAS NEVER"
      " BEEN DONE BEFORE!\n'")
sprint("Morpheus would be so proud right now.\n")
sprint("'Two Matrix Agents Wiped out like nothing'\n")
sprint("'Its Like Nothing is in your way.'\n")
sprint("'Jeez, There is so much i could say right now.'")
sprint("However this is not over just yet, You are still in the Matrix "
       "Compound.")
sprint("Get to your car quick and Contact Morpheus.\n")
sprint("Its's Time to put an end to The Matrix!\n")

input("Press ENTER to run out of the Matrix Compound.\n")
sprint("You are now out of the Matrix Compound.\n")
input("Press ENTER to run to your car.\n")
sprint("You are now outside of your car.\n")
input("Press ENTER to get inside your car.\n")
sprint(f"You are now inside the {player.car.model}.\n")
enter()

# Last Scene
print(f"{ai}\n")
sprint("Great!, You made it to your car safe and sound, Now contact Morpheus"
      " and Finish this B*TCH.\n")
input("Press ENTER to call Morpheus.\n")

print(f"{npc}\n")
sprint(f"'{player.name}!'\n")
print(f"{player.name}:\n")
sprint("Yes Morpheus it's me, I've retrieved the file!\n")
print(f"{npc}\n")
sprint("HAHAHA!\n")
sprint("I knew you wouldn't let me down.\n")
sprint(f"Now, where are you {player.name}?\n")
print(f"{player.name}:\n")
sprint("Im Near the Matrix Base.\n")
print(f"{npc}\n")
sprint("Okay okay, Now listen, We still have to upload the files to Finish this"
      " off.\n")
sprint("I will send you the location of my safehouse right now.\n")
sprint("Get here as fast as you can, And make sure you are not being followed"
       ".\n")
sprint("The Matrix Will be searching for you with their full force, So this is"
      " not over just yet.\n")
sprint(f"You've done me proud {player.name}.\n")
sprint("Now Get to my location fast.\n")

print(f"{npc}\n")
sprint("SafeHouse Location : 51420 Hwy 97, La Pine \n")

print(f"{ai}\n")
sprint("No time to stare, Now DRIVE!\n")

input("Press ENTER to drive.\n")
sprint(f"You are now driving the {player.car.model}.\n")
player.car.drive(100)

sprint("Time : 11:40pm")
sprint("Location : Somwhere in California\n")

input("Press ENTER to continue.\n")
sprint("Mission continues ...\n")

sprint("Time : 12:35pm")
sprint("Location : 51420 Hwy 95, La Pine\n")

print(f"{ai}\n")
sprint("You made it to Safehouse Safe and sound!\n")
sprint("Now Get out and go to Morpheus Quick!\n")
input("Press ENTER to get out of car.\n")
input("Press ENTER to run to the Safehouse.\n")
sprint("You are now outside of the Safehouse.\n")
input("Press ENTER to knock.\n")
sprint("KNOCK KNOCK KNOCK \n")
sprint("'Morpheus?'\n")
sprint("The Door slowly opens...")

print(f"{am}\n")
sprint("Hahaha, You really thought the Matrix was that easy to take down.\n")
sprint(f"HAND ME OVER THE STICK OR MORPHEUS DIES {player.name}!\n")
print(f"{npc}\n")
sprint("DON'T GIVE IT!\n")

print(f"{ai}\n")
sprint("'This is a mess.'\n")
sprint(f"{player.name} Agent Myth somehow found out the Safehouse location and"
      " knew you were going to be there.\n")
sprint("However there is no time to think about that now!\n")
sprint("Agent Myth is holding a gun to Morpheus's head.\n")
sprint("You cannot give the stick to him no matter what!\n")
sprint("The World is at your hands.\n")

sprint("Agent Myth may be the best the Matrix has, However he is just a human"
      " after all.\n")
sprint(f"I belive you can outsmart him {player.name}.\n")
sprint("Your next decision could determine the fate of humankind.\n")

print("Now make your move.\n")
print("Do you: \n")

Move = input("[A] Toss the Stick On the Floor.\n[B] Hand him the Stick then "
             "Knock him out.\n\n").lower()

while True:
    if Move == 'a':
        print(f"{player.name}:\n")
        sprint("'Fine Take the Stick!'\n")
        sprint("You Toss the Stick on the Floor, And Agent Myth instantly "
               "reaches for the Stick!\n")
        print(f"{npc}\n")
        sprint("'Take That B*TCH!'\n")
        print(f"{ai}\n")
        sprint("Morpheus Kicks Agent Myth as he reaches for the Stick.\n")
        sprint("This is it!, The Final Battle ...\n")
        break

    elif Move == 'b':
        print(f"{player.name}:\n")
        sprint("Fine Here you go.\n")
        sprint("POW! POW! POW\n")
        print(f"{ai}\n")
        sprint("'After everything, You do that?'\n")
        sprint("Agent Myth Shot you in the Head.\n")
        sprint("You died.")
        sprint("Mission Failed!\n")
        exit()

    else:
        sprint("Invalid Move, Make your Move!\n")
        Move = input("[A] Toss the Stick On the Floor.\n[B] Hand him the Stick"
                    " then Knock him out.\n\n").lower()


input("Press ENTER to Fight Agent Myth.\n")

sprint("\n" + "=" * 40)
sprint("\n====== FINAL BATTLE ======\n")
sprint("\n" + "=" * 40 + "\n")

sprint(f"{player.name}, Your current health is {player.HP}.")
sprint(f"Agent Myth's health is {agent_myth.HP}.\n")

Ub()

sprint("\n====== MISSION ACCOMPLISHED ======\n")

print(f"{npc}\n")
sprint("Thats it, Youv've Done it!!\n")

print(f"{ai}\n")
sprint("YOU'VE DONE IT!!!\n")
sprint("The Matrix has been Defeated.")
sprint("The fate of the World is now saved.")

# Comment every line which needs explaining
# Adjust sprint time
# Remove anu uneccessary lines
# Last - Any extra decoration
