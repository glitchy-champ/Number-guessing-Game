#Importing necessary libraries
import random
import time
import winsound

#Creating a function to handle the number guessing game
def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    # Initializing the number of attempts based on difficulty level
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    print("You can choose a difficulty level: easy (10 attempts), medium (5 attempts), or hard (3 attempts).")
    Difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
    Sound = input("Would you like to enable sound effects? (yes/no): ").lower()
    if Difficulty == "easy":
        max_attempts = 10
        print("You have chosen easy difficulty.")
    elif Difficulty == "medium":
        max_attempts = 5
        print("You have chosen medium difficulty.")
    elif Difficulty == "hard":
        print("You have chosen hard difficulty.")
        max_attempts = 3
    else:
        print("Invalid difficulty level. Defaulting to medium.")
        max_attempts = 5
    # Main game loop
    while attempts < max_attempts:
        starttime = time.time()
        # Prompting the user for their guess
        guess = input("Enter your guess: ")
        # Checking if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        # Converting the input to an integer and checking its range
        guess = int(guess)
        if guess < 1 or guess > 100:
            if Sound == 'yes':
                winsound.Beep(1000, 500)
            print("Your guess is out of range. Please guess a number between 1 and 100.")
            continue
        # Checking if the guess is correct.
        elif guess == number:
            endtime = time.time()
            if Sound == 'yes':
                winsound.Beep(2000, 500)
            time_taken = endtime - starttime
            time_taken = int(time_taken)
            print("Time taken for this guess: " + str(time_taken) + " seconds")
            print("Congratulations! You've guessed the number!")
            #Asking the user if they want to play again
            print('Would you like to play again? (yes/no)')
            play_again = input().lower()
            if play_again == 'yes':
                # Restarting the game
                guess_number()
            else:
                print("Thanks for playing!")
                return
        # Checking if the guess is too low or too high
        elif guess < number:
            if Sound == 'yes':
                winsound.Beep(1000, 500)
            print("Too low! Try again.")
            attempts += 1
            endtime = time.time()
            time_taken = endtime - starttime
            time_taken = int(time_taken)
            print("Attempts left: " + str(max_attempts - attempts))
            print("Time taken for this guess: " + str(time_taken) + " seconds")
        else:
            if Sound == 'yes':    
                winsound.Beep(1000, 500)
            print("Too high! Try again.")
            attempts += 1
            endtime = time.time()
            time_taken = endtime - starttime
            time_taken = int(time_taken)
            print("Attempts left:" + str(max_attempts - attempts))
            print("Time taken for this guess: " + str(time_taken) + " seconds")
        if attempts == max_attempts:
            # If the user has used all their attempts, reveal the number and ask if they want to play again
            if Sound == 'yes':
                winsound.Beep(500, 500)
            print(f"Sorry, you've used all your attempts. The number was {number}.")
            print('Would you like to play again? (yes/no)')
            play_again = input().lower()
            if play_again == 'yes':
                # Restarting the game
                guess_number()
            else:
                print("Thanks for playing!")
                break
# Starting the game
guess_number()
