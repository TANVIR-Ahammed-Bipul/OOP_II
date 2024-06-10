#create a number guessing game where the program randomly selects a number between 1 and 100 , and the player has to guess the number the number.the program should provide feedback indicating whether the guess is too low, too high, or correct. Use while loop to allow the player the player to keep guessing until they guess the correct number. Use if-else  statements to provide the feedback


import random

def number_guessing_game():
    
    number_to_guess = random.randint(1, 100)
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    while not guessed_correctly:
        try:
            
            guess = int(input("Enter your guess: "))

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the correct number!")
                guessed_correctly = True
        except ValueError:
            
            print("Invalid input. Please enter a valid number between 1 and 100.")

if __name__ == "__main__":
    number_guessing_game()
