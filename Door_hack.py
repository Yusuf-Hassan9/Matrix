import random

import sys,time

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0./9)

# Function for the hacking mini-game with unique attempts for each digit
def hack_door():
    # Generate a random 3-digit code
    code = [random.randint(1, 4) for _ in range(3)]
    attempts_per_digit = [4, 4, 3]  # Unique attempts for each digit
    correct_guesses = 0  # Track the number of consecutive correct guesses

    # Display instructions with enhanced formatting
    sprint("\n" + "=" * 60)
    sprint("          HACKING : THE SECURITY LOCK")
    sprint("=" * 60)
    sprint("\n> You need to guess the 3-digit code one digit at a time.")
    sprint("> Each digit is between 1 and 4. You must guess the digits in order.")
    sprint("> Guess correctly three times in a row to unlock the door.\n")
    sprint(f"> Unique attempts: Digit 1: {attempts_per_digit[0]}, Digit 2: {attempts_per_digit[1]}, Digit 3: {attempts_per_digit[2]}\n")
    sprint("=" * 60 + "\n")

    # Main game loop for each digit
    for digit_index in range(3):
        attempts = attempts_per_digit[digit_index]  # Get attempts for the current digit
        for attempt in range(1, attempts + 1):
            # Display the hacking interface
            sprint("\n" + "-" * 60)
            sprint(f" ATTEMPT {attempt} OF {attempts}  |  STATUS: {'_' if correct_guesses < 3 else 'UNLOCKED'}")
            sprint("-" * 60)
            sprint(f" Current Progress: {' '.join(['_' if i >= correct_guesses else str(code[i]) for i in range(3)])}")
            sprint("-" * 60 + "\n")

            # Prompt the player to input a guess for the current digit
            guess = input(f"[HACKER INPUT] Guess digit {digit_index + 1}: ")

            # Validate the input
            if len(guess) != 1 or not guess.isdigit():
                sprint("\n[ERROR] Invalid input. Please enter a single digit (1-4).\n")
                continue

            # Convert the guess to an integer
            guess_digit = int(guess)

            # Check if the guess is correct for the current position
            if guess_digit == code[digit_index]:
                sprint("\n" + "=" * 60)
                sprint(f"[ACCESS GRANTED] Digit {digit_index + 1} is correct.")
                sprint("=" * 60 + "\n")
                correct_guesses += 1  # Move to the next digit
                break  # Break out of the attempts loop for the next digit

            else:
                sprint("\n" + "=" * 60)
                sprint(f"[ACCESS DENIED] Digit {digit_index + 1} is incorrect.")
                sprint("=" * 60 + "\n")

            # If the player runs out of attempts for the current digit
            if attempt == attempts:
                sprint("\n" + "#" * 60)
                sprint(f"###   FAILURE! YOU'VE USED ALL ATTEMPTS FOR DIGIT {digit_index + 1}.   ###")
                sprint("#" * 60 + "\n")
                return False  # Hacking failed

    # If the player successfully guesses all digits
    sprint("\n" + "#" * 60)
    sprint("###   SUCCESS! THE DOOR IS UNLOCKED AND YOU GAIN ACCESS.   ###")
    sprint("#" * 60 + "\n")
    return True  # Hacking succeeded


# Vault Hack
def hack_vault():
    # Generate a random 4-digit code
    code = [random.randint(1,4) for _ in range(4)]
    attempts_per_digit = [4, 3, 4, 3]  # Unique attempts for each digit
    correct_guesses = 0  # Track the number of consecutive correct guesses

    # Display instructions with enhanced formatting
    sprint("\n" + "=" * 60)
    sprint("        HACKING : THE VAULT")
    sprint("=" * 60)
    sprint("\n> You need to guess the 4-digit code one digit at a time.")
    sprint("> Each digit is between 1 and 4. You must guess the digits in order.")
    sprint("> Guess correctly four times in a row to unlock the Vault.\n")
    sprint(f"> Unique attempts: Digit 1: {attempts_per_digit[0]}, Digit 2: {attempts_per_digit[1]}, Digit 3: {attempts_per_digit[2]}, Digit 4: {attempts_per_digit[3]}\n")
    sprint("=" * 60 + "\n")

    # Main game loop for each digit
    for digit_index in range(4):
        attempts = attempts_per_digit[digit_index]  # Get attempts for the current digit
        for attempt in range(1, attempts + 1):
            # Display the hacking interface
            sprint("\n" + "-" * 60)
            sprint(f" ATTEMPT {attempt} OF {attempts}  |  STATUS: {'_' if correct_guesses < 3 else 'UNLOCKED'}")
            sprint("-" * 60)
            sprint(f" Current Progress: {' '.join(['_' if i >= correct_guesses else str(code[i]) for i in range(4)])}")
            sprint("-" * 60 + "\n")

            # Prompt the player to input a guess for the current digit
            guess = input(f"[HACKER INPUT] Guess digit {digit_index + 1}: ")

            # Validate the input
            if len(guess) != 1 or not guess.isdigit():
                sprint("\n[ERROR] Invalid input. Please enter a single digit (1-4).\n")
                continue

            # Convert the guess to an integer
            guess_digit = int(guess)

            # Check if the guess is correct for the current position
            if guess_digit == code[digit_index]:
                sprint("\n" + "=" * 60)
                sprint(f"[ACCESS GRANTED] Digit {digit_index + 1} is correct.")
                sprint("=" * 60 + "\n")
                correct_guesses += 1  # Move to the next digit
                break  # Break out of the attempts loop for the next digit

            else:
                sprint("\n" + "=" * 60)
                sprint(f"[ACCESS DENIED] Digit {digit_index + 1} is incorrect.")
                sprint("=" * 60 + "\n")

            # If the player runs out of attempts for the current digit
            if attempt == attempts:
                sprint("\n" + "#" * 60)
                sprint(f"###   FAILURE! YOU'VE USED ALL ATTEMPTS FOR DIGIT {digit_index + 1}.   ###")
                sprint("#" * 60 + "\n")
                return False  # Hacking failed

    # If the player successfully guesses all digits
    sprint("\n" + "#" * 60)
    sprint("###   SUCCESS! THE VAULT IS UNLOCKED AND YOU GAIN ACCESS.   ###")
    sprint("#" * 60 + "\n")
    return True  # Hacking succeeded
