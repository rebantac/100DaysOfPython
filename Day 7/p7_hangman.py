import random

import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

# print("Choosen word: ", chosen_word)

display = []
for i in range(word_length):
    display.append("_")

while "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already entered {guess}.")
    else:
        # Checking guessed letter
        for index in range(word_length):
            letter = chosen_word[index]
            if letter == guess:
                display[index] = letter

        print(f"{''.join(display)}")

        if guess not in chosen_word:
            print(f"{guess} is not present in the word. You lose a life.")
            lives -= 1
            print(hangman_art.stages[lives])

            if lives == 0:
                print("You Lose!")
                break

    if "_" not in display:
        print("You Win!")
