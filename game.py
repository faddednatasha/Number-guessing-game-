import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    win = False

    print("--- 🎮 Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    while not win:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🥳 Correct! You found it in {attempts} attempts.")
                win = True
        except ValueError:
            print("Please enter a valid whole number.")

if __name__ == "__main__":
    play_game()
