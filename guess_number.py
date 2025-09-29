import random

def number_guessing_game():
    """Generates a random number and lets the user guess it."""
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_guess = input("Take a guess: ")
        
        # Validate user input
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        # Check if the guess is in range
        if user_guess < 1 or user_guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        attempts += 1

        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
