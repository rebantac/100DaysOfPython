############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run


import random, os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# balance = int(input("Enter balance: Rs."))



def play_blackjack():
    os.system('cls')
    from p11_art import logo
    print(logo)

    player = []
    dealer = []

    # player.append(random.choice(cards))
    player.append(11)
    player.append(random.choice(cards))

    dealer.append(random.choice(cards))
    dealer.append(random.choice(cards))

    player_score = sum(player)
    dealer_score = sum(dealer)

    print(f"Your cards: {player}. Current Score: {player_score}")
    print("Dealer's first card: ", dealer[0])

    flag = "y"
    while flag == "y":
        player_choice = input("Type 'hit' or 'stand': ")

        if player_choice == "hit":
            player.append(random.choice(cards))
            player_score = sum(player)
            print(f"Your cards: {player}. Current Score: {player_score}")
            print("Dealer's first card: ", dealer[0])

            if player_score > 21: 
                if 11 in player: # checking if player has a ace 
                    player[player.index(11)] = 1
                    player_score = sum(player)
                    print(f"Your cards: {player}. Current Score: {player_score}")
                else:
                    print("Bust! You Lose.")
                    flag = "n"

        elif player_choice == "stand":
            flag = "n"
            while dealer_score <= 17:
                dealer.append(random.choice(cards))
                dealer_score = sum(dealer)
            
            print(f"Your cards: {player}. Current Score: {player_score}")
            print(f"Dealer's cards: {dealer}. Dealer's Score: {dealer_score}")

            if dealer_score > 21:
                print("You Win!")
            elif dealer_score <= 21:
                if dealer_score > player_score:
                    print("You Lose!")
                elif dealer_score < player_score:
                    print("You Win!")
                elif dealer_score == player_score:
                    print("Its a draw!")
                

base_flag = input("Do you want to play Blackjack? Type 'y' to play: ")
while base_flag == "y":
    play_blackjack()

    base_flag = input("Do you want to play another round? Type 'y' to play: ")
