
# The Message Delay Function
'''
sys is used for writing output directly to the console.
time is used to introduce a delay between the appearance of each character.
'''

import sys,time


# Defines the function sprint,
# which takes one argument str (a string to be displayed).


def sprint(str):

   
   # Iterates over each character (c) in the string str,
   # including a newline (\n) added at the end for formatting.
   

   for c in str + '\n':

     
     # Writes the character c to the console.
     # without automatically adding a newline or buffering.
     

     sys.stdout.write(c)

     
     # Ensures the character is immediately displayed on the screen by flushing the output buffer.
     

     sys.stdout.flush()

     
     # Introduces a delay of 0.00001 seconds (10 microseconds) between each character to simulate a typewriter effect.
     

     time.sleep(0.07)


# Error Validation

# Defines a function get_valid_input that:
# Takes a prompt (a message to display to the user) and
# An options list containing valid input choices.


def get_valid_input(prompt, options):
    """Helper function to get a valid input from the player."""
    while True:
        
        # Prompts the user for input:
        # Converts the input to lowercase using .lower() to make the comparison case-insensitive.
        # Removes any leading or trailing spaces using .strip() to handle accidental whitespace.
        

        choice = input(prompt).lower().strip()

        
        # Checks if the input is valid:
        # If the user input matches one of the allowed options in the options list,
        # it returns the input, exiting the function.
        

        if choice in options:
            return choice

        # Handles empty input
        elif choice == '':
            sprint("You didn't enter anything. Please choose a valid option!\n")
        
        # Handles incorrect input
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
  


       
