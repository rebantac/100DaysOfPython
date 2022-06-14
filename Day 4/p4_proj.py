import random

options = ["Rock", "Paper", "Scissor"]

print("Type 0 -> Rock, 1 -> Paper, 2 -> Scissor")
user_choice = int(input("Enter option: "))

computer_choice = random.randint(0, 2)

print(f"You choose {options[user_choice]} and computer choose {options[computer_choice]}")

if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif user_choice == computer_choice:
    print("Its a Draw!")
elif user_choice > computer_choice:
    print("You Win!")
else:
    print("You Lose!")