import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    while True:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Correct! You guessed the number.")

guessing_game()  # Uncomment to play the game
