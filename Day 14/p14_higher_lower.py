import random
import os

import p14_art
from p14_game_data import data

def play_game():
    score = 0
    option_a = random.choice(data)
    
    while 1:
        os.system('cls')
        print(p14_art.logo)

        option_b = random.choice(data)

        if option_a == option_b:
            option_b = random.choice(data)

        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
        print(p14_art.vs)
        print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

        user_choice = input("Who has more followers? Type 'A' or 'B': ")

        if option_a['follower_count'] > option_b['follower_count']:
            if user_choice == "A":
                score += 1
            else:
                return score
        else:
            if user_choice == "A":
                return score
            else:
                score += 1
        
        option_a = option_b

final_score = play_game()
os.system('cls')
print(f"Game over! Final score: {final_score}")