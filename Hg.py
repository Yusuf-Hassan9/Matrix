import random

from Fnc import *

# Door hacking game function
def hack_door():
    # Generate a random 3-digit code with each digit, 
    # randomly chosen between 1 and 4.
    code = [random.randint(1, 4) for _ in range(3)]
    attempts_per_digit = [4, 4, 3]
    correct_guesses = 0

    # Decoration and rules
    print("\n" + "=" * 60)
    sprint("          HACKING : THE SECURITY LOCK")
    print("=" * 60)
    sprint("\n> You need to guess the 3-digit code one digit at a time.")
    sprint("> Each digit is between 1 and 4. Run out of attempts for any digit and you fail.")
    sprint("> Guess all digits correctly to unlock the door.\n")
    print("=" * 60 + "\n")

    # Iterate the outer loop over the 3 digits of the code
    for digit_index in range(3):
        attempts = attempts_per_digit[digit_index]
        for attempt in range(1, attempts + 1):

            # Display the current attempt and status of the door lock.
            # If the player hasn’t guessed all 3 digits (correct_guesses < 3),
            # status is LOCKED.
            # Otherwise, it’s UNLOCKED.
            print("\n" + "-" * 60)
            sprint(f" ATTEMPT {attempt} OF {attempts}  |  STATUS: {'LOCKED' if correct_guesses < 3 else 'UNLOCKED'}")
            print("-" * 60)

            # Show the player's progress:
            # For digits they haven’t guessed (i >= correct_guesses), display _.
            # For digits they’ve guessed correctly, display the actual digit from code.
            sprint(f" Current Progress: {' '.join(['_' if i >= correct_guesses else str(code[i]) for i in range(3)])}")
            print("-" * 60 + "\n")

            # Prompt the player to input their guess for the current digit (1-based indexing).
            while True:  # Loop until valid input is received
                guess = input(f"[HACKER INPUT] Guess digit {digit_index + 1}: ")

                # Check if the input is empty or has a length other than 1.
                if not guess or len(guess) != 1:
                    sprint("\n[ERROR] Input cannot be empty and must be a single digit.\n")
                    continue

                # Check if the input is a digit and between 1 and 4.
                if guess.isdigit():
                    guess_digit = int(guess)
                    if 1 <= guess_digit <= 4:  # Ensure the guess is within the valid range.
                        break  # Exit the loop when valid input is received.
                    else:
                        sprint("\n[ERROR] Invalid input. Please enter a digit between 1 and 4.\n")
                else:
                    sprint("\n[ERROR] Invalid input. Please enter a valid digit.\n")

            # Check if the guess is correct for the current position.
            if guess_digit == code[digit_index]:
                print("\n" + "=" * 60)
                sprint(f"[ACCESS GRANTED] Digit {digit_index + 1} is correct.")
                print("=" * 60 + "\n")

                # Increment the count of correct guesses.
                correct_guesses += 1
                break  # Exit the inner loop early if the player guesses the digit correctly.

            # Displays a message if the player's guess for the current digit is wrong.
            else:
                print("\n" + "=" * 60)
                sprint(f"[ACCESS DENIED] Digit {digit_index + 1} is incorrect.")
                print("=" * 60 + "\n")

            # If the player uses all attempts for the current digit without guessing correctly,
            # displays a failure message and exits the function (hacking failed).
            if attempt == attempts:
                print("\n" + "#" * 60)
                sprint(f"###   FAILURE! YOU'VE USED ALL ATTEMPTS FOR DIGIT {digit_index + 1}.   ###")
                print("#" * 60 + "\n")
                return False

        # Ends the outer loop early if the player guesses all 3 digits correctly.
        if correct_guesses == 3:
            break

    # Displays a message if the player gets all digits correct
    print("\n" + "#" * 60)
    sprint("###   SUCCESS! THE DOOR IS UNLOCKED AND YOU GAIN ACCESS.   ###")
    print("#" * 60 + "\n")
    return True



# Vault Hacking game function
def hack_vault():
   
    # Generate a random 4-digit code with each digit randomly chosen between 1 and 4.
    # Specify the number of attempts allowed per digit.
    # Track the number of digits the player has guessed correctly in order.
    

    code = [random.randint(1, 4) for _ in range(4)]
    attempts_per_digit = [4, 3, 4, 3]  
    correct_guesses = 0 

    # Decoration and Rules
    print("\n" + "=" * 60)
    sprint("        HACKING : THE VAULT")
    print("=" * 60)
    sprint("\n> You need to guess the 4-digit code one digit at a time.")
    sprint("> Each digit is between 1 and 4. You must guess the digits in order.")
    sprint("> Guess all digits to unlock the Vault.\n")
    print("=" * 60 + "\n")

    # Iterate the outer loop over the 4 digits of the code
    for digit_index in range(4):
        attempts = attempts_per_digit[digit_index]  # Get attempts for the current digit
        for attempt in range(1, attempts + 1):

            # Display the current attempt and status of the door lock.
            # If the player hasn’t guessed all 4 digits (correct_guesses < 4),
            # status is LOCKED. Otherwise, it’s UNLOCKED.
            print("\n" + "-" * 60)
            sprint(f" ATTEMPT {attempt} OF {attempts}  |  STATUS: {'LOCKED' if correct_guesses < 4 else 'UNLOCKED'}")
            print("-" * 60)

            # Show the player's progress:
            sprint(f" Current Progress: {' '.join(['_' if i >= correct_guesses else str(code[i]) for i in range(4)])}")
            print("-" * 60 + "\n")

            # Prompt the player to input their guess for the current digit (1-based indexing).
            while True:  # Loop until valid input is received
                guess = input(f"[HACKER INPUT] Guess digit {digit_index + 1}: ")

                # Check if the input is empty or has a length other than 1.
                if not guess or len(guess) != 1:
                    sprint("\n[ERROR] Input cannot be empty and must be a single digit.\n")
                    continue

                # Check if the input is a digit and between 1 and 4.
                if guess.isdigit():
                    guess_digit = int(guess)
                    if 1 <= guess_digit <= 4:  # Ensure the guess is within the valid range.
                        break  # Exit the loop when valid input is received.
                    else:
                        sprint("\n[ERROR] Invalid input. Please enter a digit between 1 and 4.\n")
                else:
                    sprint("\n[ERROR] Invalid input. Please enter a valid digit.\n")

            # Check if the guess is correct for the current position.
            if guess_digit == code[digit_index]:
                print("\n" + "=" * 60)
                sprint(f"[ACCESS GRANTED] Digit {digit_index + 1} is correct.")
                print("=" * 60 + "\n")

                # Increment the count of correct guesses.
                correct_guesses += 1  
                break  # Exit the inner loop early if the player guesses the digit correctly.

            # Displays a message if the player's guess for the current digit is wrong.
            else:
                print("\n" + "=" * 60)
                sprint(f"[ACCESS DENIED] Digit {digit_index + 1} is incorrect.")
                print("=" * 60 + "\n")

            # If the player uses all attempts for the current digit without guessing correctly,
            # displays a failure message and exits the function (hacking failed).
            if attempt == attempts:
                print("\n" + "#" * 60)
                sprint(f"###   FAILURE! YOU'VE USED ALL ATTEMPTS FOR DIGIT {digit_index + 1}.   ###")
                print("#" * 60 + "\n")
                return False 

    # If the player successfully guesses all digits, display a success message.
    print("\n" + "#" * 60)
    sprint("###   SUCCESS! THE VAULT IS UNLOCKED AND YOU GAIN ACCESS.   ###")
    print("#" * 60 + "\n")
    return True

