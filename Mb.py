import random

from cc import *

                                                            ## ALL THE 'SCENES' - MATRIX BASE AND COMPOUND ##



def Gettinin(): # Getting into the Matrix Base Compound Scene #
    sprint("Do you: \n")
    Move1 = get_valid_input("[A] Climb The Fence into the Compound? \n[B]"
                           " Enter through the Back Entrance Using "
                            "Stealth?\n", ['a', 'b']).lower()
    while True:
        if Move1 == 'a':
            # Fence Approach
            sprint("You begin climbing the Fence behind the Container.\n")
            sprint("You find yourself in a situation as you get to the top of the"
                   " Fence.\n")
            sprint("The fence is lined with sharp spikes, something you had not"
                   " noticed before.\n")
            sprint("There is no turning back now!\n")
        
            print("Do you:\n")
            Move = get_valid_input("[A] Try to hurdle over the spikes?\n[B] Look"
                    " for a way to cover the spikes?\n", ['a', 'b']).lower()

            while True:
                if Move == 'a':
                    # Option to hurdle over the spikes
                    sprint("You brace yourself and prepare to leap over the spikes."
                           "\n")
                    sprint("With a burst of energy, you jump, trying to clear the "
                           "sharp points...\n")
                    hurdle_success = random.choice([True, False]) # Random chance for success
        
                    if hurdle_success:
                        sprint("You manage to Successfully Hurdle over the spikes."
                               "\n")
                        print(f"'{player.name} you Really avoided those spikes like"
                              "a Ninja'")
                        sprint("You can see a entrance into the Building.\n")
                        input("Press ENTER to go to the entrance \n")
                        sprint("You are now at the entrance, And to your suprise"
                               " there are"
                               " no Matrix Guards to be seen.\n")
                        input("Press ENTER to go inside the Matrix Base \n")
                        break
                    
                    else:
                        sprint("You leap, but your leg catches one of the"
                              " spikes!\n")
                        sprint("You manage to pull yourself over, but you are"
                              " bleeding from a nasty cut.\n")
                        player.HP -= 20  # Reduce player's health
                        sprint(f"{player.name}, you lose 20 HP. Current HP: "
                               f"{player.HP}\n")
                        sprint("You have to patch up the Wound.\n")
                        input("Press ENTER to patch up wound \n")
                        player.HP -= 20  # Give Back Health
                        sprint("You Found some Cloth in the Container and used it"
                               " to patchup your wound.\n")
                        sprint("Your leg will be fine for now.\n")
                        sprint("You can see a entrance into the Building.\n")
                        input("Press ENTER to go to the entrance \n")
                        sprint("You are now at the entrance, And to your suprise"
                              " there are no Matrix Guards to be seen.\n")
                        input("Press ENTER to go inside the Matrix Base \n")
                        break

                elif Move == 'b':
                    # Option cover the spikes
                    sprint("You carefully look around the top of the fence for"
                          " something to help.\n")
                    sprint("To your luck you spot a little branch from the tree,"
                          " You grab the Little Branch.\n")
                    sprint("It is not perfect, but it should work and prevent"
                           " anything from happening.\n")
                    sprint("You climb over using the Branch as cover, avoiding the"
                     " sharp points, and you make it to the other side safely!\n")
                    print(f"{ai}\n")
                    sprint("'Good thinking! You avoided injury.'\n")
                    sprint("You can see a entrance into the Building.\n")
                    input("Press ENTER to go to the entrance \n")
                    sprint("You are now at the entrance, And to your suprise there"
                          " are no Matrix Guards to be seen.\n")
                    input("Press ENTER to go inside the Matrix Base \n")
                    break

                else:
                    sprint("Invalid Choice, Choose a option!\n") # 'Error Validation' #
                
            break

        elif Move1 == 'b':
            # Stealth Approach
            sprint("You decide to sneak towards the back entrance.\n")
            sprint("Keeping low to the ground, you move silently in the shadows.\n")
            sprint("As you get closer, you spot a Matrix Guard near the entrance.\n")
            sprint("You will need to Deal with the Matrix Guard to Enter the "
                   " Building."
                   "\n")

            print("Do you :\n")
            Move = input("[A] Distract the Matrix Guard?\n[B] Wait for the Matrix"
                        " Guard to turn away, Then take him out quickly?\n").lower()

            while True:
                if Move == 'a':
                    sprint("You Find some Pebbles on the ground, You then use the"
                          " Pebbles to distact the guard by throwing them.\n")
                    sprint("You swiftly Begin Moving to the Entrance.\n")
                    Entrance_success = random.choice([True, False]) # Random chance for success

                    if Entrance_success:
                        sprint("Luckily, You make it to the Entrance without getting"
                              "caught.\n")
                        input("Press ENTER to go inside the Matrix Base")
                        sprint("You slip through the entrance unnoticed. Good"
                               " work!\n")
                        break

                    else:
                        sprint("The Matrix Guard Heard one of your footsteps as"
                               " you were moving.\n")
                        print(f"{mg}\n")
                        sprint("'WHO ARE YOU!'\n")
                        print(f"{ai}\n")
                        sprint("The Matrix Guard is approaching you.\n")
                        sprint("Your back is faced towards him.\n")
                        sprint("The Matrix Guard is Right Behind you now and is"
                              " pointing a Gun at you.\n")

                        print("Do you : \n")  # Taking out The Matrix Guard Mini Scene #
                        Move = get_valid_input("[A] Turn and Knock Out the Henchman"
                         " using your Fists?\n[B] Turn and Reach for your Weapon to"
                         " take him out?\n", ['a', 'b'])

                        while True:
                            if Move == 'a':
                               sprint(f"{player.name} you turn around smoothly and"
                                " give the Matrix Guard a punch right on the nose."
                                "\n")
                               sprint("The Matrix Guard was Instantly Knocked out "
                                      "Clean!\n")
                               print(f"{ai}\n")
                               sprint("What a Hit, I am Certainly Impressed. \n")
                               sprint(f"{player.name} you must quickly tie up this"
                                     " body, Then head into the Base. \n")
                               input("Press ENTER to tie up the Matrix Guards Body"
                                    "\n")
                               sprint("The Matrix Guards body has been dealt with."
                                      "\n")
                               input("Press ENTER to go inside the Matrix Base \n")
                               break

                            elif Move == 'b':
                                sprint("You Turned Around Smoothly, However as you"
                                       " reached for your weapon.\n")
                                sprint("The Matrix Guard fired right away, This"
                                       " instantly knocked you out cold.\n")
                                sprint("Later you woke up surrounded by Matrix "
                                       "Agents, Captured.")
                                sprint(f"'{player.name} you were so close! \n")
                                sprint("Mission Failed.")
                                exit()
                           
                elif Move == 'b':
                    sprint("You wait for the Matrix Guard to turn around and Knock"
                          " him out clean.\n")
                    input("Press ENTER to hide the Matrix Guard's Body.\n")
                    sprint("The Matrix Guards's Bod was hidden.\n")
                    input("Press ENTER to go inside the Matrix Base.\n")
                    break

            break  # End of Scene # 


def Infiltration(): # Infiltrating and Finding the Files Room Scene #
    print("Do you: \n")
    Move = input("[A] Take the Staircase Upstairs?\n[B] Take the Staircase "
                 "Downstairs?\n").lower()

    while True:
        if Move == 'a':
            sprint("You take the staircase Upstairs.")
            sprint("However, there is a Matrix Guard.\n")
            print(f"{player.name} you can use this as a opportunity to find out"
                 " where the Files room is.\n")

            print("Do you :\n")  # Handling The Guard Mini Scene #
            Move = input("[A] Sneak up behind and point your weapon to his head?"
                         "\n[B] Stay Hidden for abit and watch the guard?\n").lower()

            if Move == 'a':
                sprint("You sneak up to the guard from behind, moving as silently as"
                       " possible.\n")
                sprint("You press your weapon to the back of his head and speak in a"
                       " low voice.\n")
                print(f"{player.name}:\n")
                sprint("'Where is the files room?' \n")
                sprint("'You have 5 seconds to tell me or your dead!'\n")
                print(f"{mg}\n")
                sprint("'Please dont shoot me!' \n")
                sprint("'If you want to go to the files room, Go Downstairs '\n")
                sprint("'then take a right and go down to the end of the corridor!'"
                       "\n")
                sprint("'Now Please let me GO'\n")
                print(f"{player.name}:\n")
                sprint("'Not just Yet'\n")
                input("Press ENTER to hit the Matrix Guard and make him unconscious."
                      "\n")
                sprint("The Matrix Guard is now unconscious. \n")
                input("Press ENTER to Hide the Matrix Guard. \n")
                sprint("The Matrix Guard is now hidden.\n")
                print(f"{ai}\n")
                sprint("'Good Work there.'\n")
                sprint("'You now know where to find the files room'\n")
                sprint("'You must hurry and get there, Before the Matrix guard wakes"
                       " up and the whole place is alerted!'\n")
                input("Press ENTER to go Downstairs\n")
                sprint("You are now Downstairs \n")
                break

            elif Move == 'b':
                sprint("You decide to stay hidden and observe the guard for a"
                      "moment."
                       "\n")
                sprint("The Matrix guard is now talking into his earpiece.\n")
                print(f"{mg}\n")
                sprint("'Boss said im switching with you in 20 mins to guard the"
                       " files room...'\n")
                sprint("'I've never actually guarded the files rooom before ...'"
                       "\n")
                sprint("'All i know is that its all the way downstairs and on the"
                        " right'\n")
                sprint("'Alright yes, I will be there in 30 mins'\n")
                print(f"{ai}\n")
                sprint(f"'{player.name}, I think today is your lucky day.'\n")
                sprint("You hear the Matrix Guard mention something about a security"
                       " shift change and the location of the Files room.\n")
                sprint("It looks like your patience paid off.\n")
                sprint("'You now know where to find the files room'\n")
                sprint("'You must hurry and get there'\n")
                sprint("Press ENTER to go Downstairs \n")
                sprint("You are now Downstairs\n")
                break

            else:
                sprint("Invalid Choice, Choose a option!\n")
                Move = input("[A] Sneak up behind and point your weapon to his "
                             "head?\n[B]"
                         " Stay Hidden for abit and watch the guard?\n").lower()

        elif Move == 'b':
            # Player takes the staircase downstairs
            sprint("You decide to take the staircase downstairs.\n")
            sprint(f"{player.name}, you hear faint footsteps approaching from around"
                   " the corner.\n")
            sprint("You peek your head and see that there is a Matrix guard.\n")
            print(f"{player.name} you can use this as a opportunity to find out where"
                  " the Files room is. \n")

            print("Do you :\n")  # Handling The Guard Mini Scene #
            Move = input("[A] Sneak up behind and point your weapon to his head?"
                    "\n[B] Stay Hidden for abit and watch the guard?\n").lower()
            while True:
                if Move == 'a':
                    sprint("You sneak up to the guard from behind, moving as"
                           " silently as possible.\n")
                    sprint("You press your weapon to the back of his head and speak"
                          " in a low voice.\n")
                    print(f"{player.name}:\n")
                    sprint("'Where is the files room?' \n")
                    sprint("'You have 5 seconds to tell me or your dead!'\n")
                    print(f"{mg}\n")
                    sprint("'Please dont shoot me!' \n")
                    sprint("'The files room is on the right at the end of this"
                           " corridor!"
                           "'\n")
                    sprint("'Now Please let me GO'\n")
                    print(f"{player.name}:\n")
                    sprint("'Not just Yet'\n")
                    input("Press ENTER to hit the Matrix Guard and make him"
                          " unconscious.\n")
                    sprint("The Matrix Guard is now unconscious.\n")
                    input("Press ENTER to Hide the Matrix Guard.\n")
                    sprint("The Matrix Guard is now hidden.\n")
                    print(f"{ai}\n")
                    sprint("'Good Work there.'\n")
                    sprint("'You now know where to find the files room'\n")
                    sprint("'Go to the files room, Before the Matrix guard wakes"
                          " up and the whole place is alerted!'\n")
    
                elif Move == 'b':
                    sprint("You decide to stay hidden and observe the guard for"
                          " a moment.\n")
                    sprint("The Matrix guard is now talking into his earpiece.\n")
                    print(f"{mg}\n")
                    sprint("'Boss said im switching with you in 20 mins to guard"
                          " the...'\n")
                    sprint("'Thats Alright, I can tell you where it is ...'\n")
                    sprint("'The files room is here, Downstairs and on the right "
                           "at the end of the corridor'\n")
                    print(f"{ai}\n")
                    sprint(f"'{player.name}, I think today is your lucky day.'")
                    sprint("You hear the Matrix Guard mention something about a "
                    "security shift change and the location of the Files room.\n")
                    sprint("It looks like your patience paid off.\n")
                    sprint("'You now know where to find the files room'\n")
                    sprint("'Hurry and get to the files room'\n")
                    break

                else:
                    sprint("Invalid Choice, Choose a option!\n")
                    Move = input("[A] Sneak up behind and point your weapon to his"
                    " head?\n[B] Stay Hidden for abit and watch the guard?\n").lower()

        else:
            sprint("Invalid Choice, Choose a option!\n")
            Move = input("[A] Take the Staircase Upstairs?\n[B] Take the Staircase"
                 " Downstairs?\n").lower()

        
    # Gettng inside the files room
    input("Press ENTER to go to the files room. \n")
    sprint(f"{player.name}, you are now infront of the files room, However you"
           " cannot get inside without a code.\n")
    sprint("This should not be a problem as you are a hacker, One of the Best"
           " Hackers in the World! \n")
    print(f"{ai}\n")
    sprint(f"{player.name}, You must quickly Bypass the door and get inside.\n")

    # End Of this Scene #


def DataStick():  # Finding the Data Stick Mini Scene #
    print("Do you: \n")
    Move = input("[A] Search The Computer Desk for the Stick?\n[B] Search the"
                 " Lockers for the Stick?\n").lower()

    # Searching the Computer
    if Move == 'a':
        sprint("You Search everywhere on the Computer desk for the drive, However"
              " it is not visible\n")

        print("Do you: \n")
        Move = input("[A] Search the Lockers for the Stick?\n[B] Look around the"
                    " room Hoping to Find it?\n").lower()

        if Move == 'a':
            sprint("You look in the lockers, But the stick is still not visible."
                   "\n")
            sprint("All you can really do now is look around the room and hope for"
                  " the best. \n")
            sprint("Time is really Running out ... \n")
            input("Press ENTER to look around the room \n")
            sprint("you are looking around desperately now, When ... \n")
            sprint("CLICK ... \n")
            sprint("You Stepped on a button which triggered a Hidden door.\n")
            sprint("On the other side of the Door is a Vault.\n")


        elif Move == 'b':
            sprint("you are looking around desperately now, When ... \n")
            sprint("CLICK ... \n")
            sprint("You Stepped on a button which triggered a Hidden door.\n")
            sprint("On the other side of the Door is a Vault. \n")

        else:
            sprint("Invalid Output!\n")
            Move = input("[A] Search the Lockers for the Stick?\n[B] Look around"
                         " the room Hoping to Find it?\n").lower()

    # Searching the Computer
    elif Move == 'b':
        sprint("You look in the lockers, But the stick is still not visible. \n")

        print("Do you: \n")
        Move = input("[A] Search The Computer Desk for the Stick?\n[B] Look around"
                    " the room Hoping to Find it?\n").lower()

        if Move == 'a':
             sprint("You Search everywhere on the Computer desk for the drive, "
                    "However the stick is still not visiible.\n")
             sprint("All you can really do now is look around the room and hope "
                    "for the best. \n")
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
            Move = input("[A] Search The Computer Desk for the Stick?\n[B] Look "
                         "around the room Hoping to Find it?\n").lower()

    else:
        sprint("Invalid Output!\n")
        Move = input("[A] Search The Computer Desk for the Stick?\n[B] Search the"
                 " Lockers for the Stick?\n").lower()


    # Getting into the Vault to get the Stick
    print(f"{ai}\n")
    sprint("'Of Course they put the stick in a Vault!' \n")
    sprint(f"'{player.name} i guess you are going to need to use your hacking "
           "skills again.'\n")
    sprint("Hack the pin of the Vault and retrieve the Stick.\n")
    sprint("Hurry, You dont have much time left now.\n")

    input("Press ENTER to go to the Vault. \n")
    sprint("You are now infront of the vault.\n")
    input("Press ENTER to hack into the Vault.\n")

    # End Of Mini Scene #

