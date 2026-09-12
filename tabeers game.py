import random

def guessing_game():
    print("====================================")
    print("      NUMBER GUESSING GAME")
    print("====================================\n")

    # Level selection
    print("Choose Difficulty Level:")
    print("1. Easy   - Range: 1 to 50   | Attempts: 10")
    print("2. Medium - Range: 1 to 100  | Attempts: 7")
    print("3. Hard   - Range: 1 to 500  | Attempts: 5\n")
    
    choice = input("Enter 1, 2 or 3: ")

    if choice == "1":
        max_range = 50
        max_attempts = 10
        level = "Easy"
    elif choice == "2":
        max_range = 100
        max_attempts = 7
        level = "Medium"
    elif choice == "3":
        max_range = 500
        max_attempts = 5
        level = "Hard"
    else:
        print("Invalid choice! Defaulting to Medium.")
        max_range = 100
        max_attempts = 7
        level = "Medium"
    
    secret_number = random.randint(1, max_range)
    attempts = 0
    
    print(f"\nYou selected {level} Mode")
    print(f"Guess the number between 1 and {max_range}")
    print(f"You have {max_attempts} attempts\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too Low! Try again.\n")
            elif guess > secret_number:
                print("Too High! Try again.\n")
            else:
                print("====================================")
                print("CONGRATULATIONS! You guessed it!")
                print(f"Secret Number: {secret_number}")
                print(f"Attempts Used: {attempts}/{max_attempts}")
                print(f"Difficulty: {level}")
                print("====================================")
                return
        except ValueError:
            print("Invalid input! Please enter a number.\n")
    
    # If loop ends = game over
    print("====================================")
    print("GAME OVER!")
    print(f"You used all {max_attempts} attempts.")
    print(f"The secret number was: {secret_number}")
    print("====================================")

# Run the game
if __name__ == "__main__":
    guessing_game()
    