import random   # Importing random module to generate random number


def guessing_game():
    
    best_score = None   # Stores minimum attempts used (Bonus feature)

    # Outer loop allows user to play again
    while True:
        
        # Computer randomly selects number between 1 and 100
        secret_number = random.randint(1, 100)
        
        attempts = 7   # User gets 7 attempts
        used_attempts = 0   # Count attempts used

        print("\nNew Game Started")
        print("Guess a number between 1 and 100")

        # Loop runs while attempts remain
        while attempts > 0:
            
            guess = int(input("Enter your guess: "))
            used_attempts += 1
            attempts -= 1

            # If guess is correct
            if guess == secret_number:
                print("Correct! You guessed it in", used_attempts, "attempts.")

                # Update best score (minimum attempts)
                if best_score is None or used_attempts < best_score:
                    best_score = used_attempts
                    print("New Best Score:", best_score)

                break   # Exit guessing loop

            # If guess is too low
            elif guess < secret_number:
                print("Too low!")

            # If guess is too high
            else:
                print("Too high!")

            # Bonus hint if guess is close (within 5)
            if abs(guess - secret_number) <= 5:
                print("Very close!")

            # Show remaining attempts
            print("Attempts remaining:", attempts)

        # If user failed after 7 attempts
        if attempts == 0 and guess != secret_number:
            print("Game Over")
            print("The correct number was:", secret_number)

        # Ask user to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("Thanks for playing")
            break   # Exit outer loop


# Run the game
if __name__ == "__main__":
    guessing_game()

