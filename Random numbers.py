import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
    print("Secret Numbers: ", secret_number)

guess_number()
