import random

def number_guessor(difficulty):
    number_thought = random.randint(1, 100)

    if difficulty == "easy":
        attempt = 10
    elif difficulty == "hard":
        attempt = 5
    
    while attempt != 0:
        print(f"You have {attempt} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        if guess > number_thought:
            print("Too high.")
            attempt -= 1
        elif guess < number_thought:
            print("Too low.")
            attempt -= 1
        else:
            print("You've guessed correct, You Win!")
            return

    if attempt == 0:
        print("Tou've run out of guesses, you lose.")
        return

        


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number_guessor(difficulty)