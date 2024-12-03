
# The Message Delay Function
import sys,time

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.00001)


def mhm(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.9)

# Error Validation
def get_valid_input(prompt, options):
    """Helper function to get a valid input from the player."""
    while True:
        choice = input(prompt).lower().strip()
        if choice in options:
            return choice
        elif choice == '':
            sprint("You didn't enter anything. Please choose a valid option!\n")
        else:
            sprint("Invalid choice. Please choose a valid option!\n")


# Dialogue names (constants)
ai = "Narrator:"
npc = "Morpheus:"
hman = "Matrix Henchman:"
hmanb = "Matrix Henchman Boss:"
mea = "Matrix Elite Agents:"
mg = "Matrix Guard:"
am = "Agent Myth:"

# Press enter to continue 
def enter():
    input("Press ENTER to Continue.\n\n")
   #sprint("Continuing... *60")


       
