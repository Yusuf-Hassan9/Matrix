from cc import * 
from Wpns import *


 ## ALL THE BATTLES - THE MATRIX ##

battle = True

def Wc():
    # Loop until player chooses correctly
    while True:
        try:
            Move1 = input("[A] Glock 19\n[B] Katana\n[C] Pump Shotgun"
                         "\n\n").lower()
            if Move1 == 'a':
                player.weapon = Weapon1("Glock 19")
                print(f"Good Choice {player.name} \n")
                break

            elif Move1 == 'b':
                print("Abit of a risky choice, But it could pay off!\n")
                player.weapon = Weapon1("Katana")
                break

            elif Move1 == 'c':
                print(f"Hit the Jackpot {player.name} \n")
                player.weapon = Weapon1("Pump Shotgun")
                break

            else:
                sprint("Invalid choice, Choose correctly!\n")
                Move1 = input("[A] Glock 19\n[B] Katana\n[C] Pump Shotgun"
                             "\n\n").lower()

        # Error Handling
        except Exception as e:
            sprint(f"There was an unexpected error: {e}\nPlease try again.\n")



def Fb():
    # First Henchman Battle
    while battle==True:
        sprint("You find yourself face-to-face with a menacing Henchman.\n")
        sprint("\n====== ENCOUNTER ======\n")
        # Giving Moves Option
        while True:
            sprint("What will you do?\n")
            print("'Attack' or 'Run'\n")
            sprint("Choose your Move :\n")
            Move3 = input("[A] Attack with Weapon\n[B] Attack With Strength\n[C]"
                         " Run Away \n\n").lower()
            if Move3 == 'a':
                player.weapon1_attack(matrix_henchman[0])
                break
            elif Move3 == 'b':
                player.attack(matrix_henchman[0])
                break
            elif Move3 == 'c':
                matrix_henchman[0].weapon2_attack(player)
                break
            else:
                print("Invalid Choice\n")
                Move3 = input("[A] Attack with Weapon\n[B] Attack With Strength\n"
                              "[C]Run Away \n\n").lower()

        # Making Player Deal Damage Throughout Battle
        henchman_choice = random.randint(1, 2)

        if henchman_choice == 1:
            matrix_henchman[0].weapon2_attack(player)
        else:
            matrix_henchman[0].attack(player)

        # Battle Health Check (Required)
        matrix_henchman[0].health_check()
        player.health_check()

        # If the Henchman Dies you Can continue
        if matrix_henchman[0].HP <= 0:
            sprint("\n====== VICTORY ======\n")
            break
     
        # If the Player dies then They have Failed
        if player.HP <= 0:
            sprint("\n====== DEFEAT ======\n")
            exit()



def Sb():
    while battle==True:
        sprint("The Henchman appears, ready to take you down!\n")
        sprint("\n====== ENCOUNTER ======\n")

    # Giving Moves Option
        while True:
            sprint("What will you do?\n")
            print("'Attack' or 'Run'\n")
            sprint("Choose your Move : \n")
            Move3 = input("[A] Attack with Weapon\n[B] Attack With Strength\n[C]"
                         " Run Away \n\n").lower()
            if Move3 == 'a':
                player.weapon1_attack(matrix_henchman[1])
                break
            elif Move3 == 'b':
                player.attack(matrix_henchman[1])
                break
            elif Move3 == 'c':
                matrix_henchman[1].weapon2_attack(player)
                break
            else:
                print("Invalid Choice\n")
                sprint("Choose your Move :\n")
                Move3 = input("[A] Attack with Weapon\n[B] Attack With Strength\n"
                              "[C] Run Away \n\n").lower()


        # Making Player Deal Damage Throughout the Battle
        henchman_choice = random.randint(1, 2)

        if henchman_choice == 1:
            matrix_henchman[1].weapon2_attack(player)
        else:
            matrix_henchman[1].attack(player)

        # Battle Health Check (Required)
        matrix_henchman[1].health_check()
        player.health_check()

        # If You Defeat Second Henchman Continue
        if matrix_henchman[1].HP <= 0:
            sprint("\n====== VICTORY ======\n")
            break

        # If the Player dies then They have Failed
        if player.HP <= 0:
            sprint("\n====== DEFEAT ======\n")
            exit()
        


def Lb():
    while battle==True:
        sprint("The Henchman Boss stands before you, a formidable opponent!\n")
        sprint("\n====== ENCOUNTER ======\n")
    # Giving Moves Option
        while True:
           sprint("What will you do?\n")
           print("'Attack' or 'Run'\n")
           sprint("Choose your Move : \n")
           Move4 = input("[A] Attack with Weapon\n[B] Attack With Strength\n[C]"
                         " Run Away \n\n").lower()
           if Move4 == 'a':
                player.weapon1_attack(henchman)
                break
           elif Move4 == 'b':
                player.attack(henchman)
                break
           elif Move4 == 'c':
                henchman.weapon2_attack(player)
                break
           else:
                print("Invalid Choice\n")
                sprint("Choose your Move :\n")
                Move4 = input("[A] Attack with Weapon\n[B] Attack With Strength"
                              "\n[C] Run Away \n\n").lower()
    # Player Deals Damage Regardless
    # Henchman either Attacks Player with Strength or Weapon
        henchman_choice = random.randint(1, 2)

        if henchman_choice == 1:
            henchman.weapon2_attack(player)
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
            sprint("\n====== DEFEAT ======\n")
            exit()



def Gb():
    while battle==True:
        sprint("The Matrix Guard is running towrds you at pace!\n")
        sprint("\n====== ENCOUNTER ======\n")

        while True:
            sprint("What will you do?\n")
            sprint("Choose your Move: \n")
            Move = input("[A] Attack with Weapon\n[B] Attack with strength"
                         "\n\n").lower()

            if Move == 'a':
                player.weapon1_attack(matrix_guard)
                break
            
            elif Move == 'b':
                player.attack(matrix_guard)
                break

            else:
                sprint(f"Inavild Escape, You cannot run from this "
                       f"{player.name}. \n")
                sprint("Choose your Move: \n")
                Move = input("[A] Attack with Weapon\n[B] Attack with "
                             "strength"
                             "\n\n").lower() 

        # Matrix Guard Attacking
        matrix_guard_choice = random.randrange(1,2)

        if matrix_guard_choice == 1:
            matrix_guard.weapon2_attack(player)

        else:
            matrix_guard.attack(player)

        # Health Check
        player.health_check()
        matrix_guard.health_check()

        # Matrix Guard Dies.
        if matrix_guard.HP <= 0:
            sprint("\n====== VICTORY ======\n")
            break

        # If player dies.
        if player.HP <= 0:
            sprint("\n====== DEFEAT ======\n")
            exit()



def Mab():
    while battle==True:
        sprint("A Matrix Agent has raised a weapon at you.\n")
        sprint("\n====== ENCOUNTER ======\n")

        while True:
            sprint("What will you do? \n")
            print("Make your Move! : \n")
            Move = input("[A] Attack with Weapon\n[B] Attack with strength"
                         "\n\n").lower()
            if Move == 'a':
                player.weapon1_attack(Matrix_agent[0])

            elif Move == 'b':
                player.attack(Matrix_agent[0])

            else:
                 sprint(f"Inavild Escape, You cannot run from this "
                        f"{player.name}. \n")
                 sprint("Choose your Move: \n")
                 Move = input("[A] Attack with Weapon\n[B] Attack with strength"
                              "\n\n").lower() 
             
            Matrix_agent_choice = random.randint(1, 2)

            if Matrix_agent_choice == 1:
               Matrix_agent[0].weapon2_attack(player)

            else:
                Matrix_agent[0].attack(player)
           
            # Health Check
            player.health_check()
            Matrix_agent[0].health_check()

            # Using the powerup
            if player.HP <= 35:
               player.powerup_attack(Matrix_agent[0])
               Matrix_agent[0].health_check()

            # Matrix Agent Dies.
            if Matrix_agent[0].HP <= 0:
                sprint("\n====== VICTORY ======\n")
                break

        print("The Matrix Agent has been defeated!\n")
        break



def Mab2():
    while battle==True:
        sprint("You dodge every single one of his Bullets.\n")
        print(f"{mea}\n")
        sprint("'IMPOSSIBLE F*CK'\n")

        while True:
            sprint("\n====== ENCOUNTER ======\n")
            sprint("The Matrix Agent Agitated now holds up two rifles at you.\n")
            print("What will you do?\n")
            print("Make your Move!: \n")
            Move = input("[A] Attack with Weapon\n[B] Attack with ?????"
                         "\n\n").lower()
            if Move == 'a':
                player.weapon1_attack(Matrix_agent[1])

            elif Move == 'b':
                player.powerup_attack(Matrix_agent[1])

            else:
                 sprint(f"Inavild Escape, You cannot run from this "
                        f"{player.name}. \n")
                 sprint("Choose your Move: \n")
                 Move = input("[A] Attack with Weapon\n[B] Attack with ?????"
                              "\n\n").lower() 
             
            Matrix_agent_choice = random.randint(1, 2)

            if Matrix_agent_choice == 1:
               Matrix_agent[1].weapon2_attack(player)

            else:
                Matrix_agent[1].attack(player)
           
            # Health Check
            player.health_check()
            Matrix_agent[1].health_check()

            if player.HP <= 0:
                sprint("\n====== DEFEAT ======\n")
                exit()

            if Matrix_agent[1].HP <= 0:
                sprint("\n====== VICTORY ======\n")
                break
        break



def Ub():
    while battle==True:
        sprint("\n====== ENCOUNTER ======\n")
        sprint("Agent Myth has grabbed you and is now punching you repeatedly!")
        sprint("Your Vision is Blurry and you can barely see now\n")
        while True:
            sprint("You need to Make a move.\n")
            print("Make your Move!:\n")
            Move = input("[A] ?????\n[B] ?????"
                         "\n\n").lower()
            if Move == 'a':
                player.powerup_attack(agent_myth)

            elif Move == 'b':
                player.weapon1_attack(agent_myth)

            else:
                 sprint(f"Inavild Escape, You cannot run from this "
                        f"{player.name}. \n")
                 sprint("Choose your Move: \n")
                 Move = input("[A] ?????\n[B] ?????"
                         "\n\n").lower()
             
            # Myth's Turn to Attack
            Agent_Myth_choice = random.randint(1, 2)

            if Agent_Myth_choice == 1:
               agent_myth.weapon2_attack(player)

            else:
                agent_myth.attack(player)
           
            # Health Check
            player.health_check()
            agent_myth.health_check()

            # Using the powerup
            if player.HP <= 0:
               sprint("Agent Myth has Ended you.\n")
               exit()

            # The Myth
            if agent_myth.HP <= 0:
               sprint("\n====== VICTORY ======\n")
               break # Exit the inner Loop
        break # Exit the Battle Loop
