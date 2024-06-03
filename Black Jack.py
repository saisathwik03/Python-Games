import random

# Function to create a deck of cards
def deck_creation():
    deck = []
    # Adding cards from 2 to 11 (excluding 12) four times each
    for i in range(2, 12):
        deck += [i] * 4  
    # Adding 10 (face cards) nine times
    deck += [10] * 12
    return deck

# Function to deal cards to players
def dealing_cards(deck):
    return [deck.pop(), deck.pop()]

# Function to calculate the score of a hand
def score_calculations(cards):
    score = sum(cards)
    # If there's an Ace in the hand and the score is over 21, count Ace as 1 instead of 11
    if 11 in cards and score > 21:
        score -= 10
    return score

# Function to manage the game logic
def game_logic(player_cards, dealer_cards, deck):

    # Calculate player's score
    player_score = score_calculations(player_cards)

    # Print initial hands
    print("Player's cards:", player_cards, "Score:", player_score)
    print("Dealer's cards:", dealer_cards[0], "Card Hidden")

    # Player's turn
    while player_score <= 21:
        action = input("Choose your play: hit or stand: ")

        if action == "hit":
            player_cards.append(deck.pop())
            player_score = score_calculations(player_cards)
            print("Player's cards:", player_cards, "Score:", player_score)
        elif action == "stand":
            break
        else:
            print("Invalid input! Please choose 'hit' or 'stand'.")

    # Dealer's turn
    print("Dealer's cards:", dealer_cards)
    print("Dealer's score:", score_calculations(dealer_cards))

    # Dealer continues to pick cards until their score is 17 or higher
    while score_calculations(dealer_cards) < 17:
        dealer_cards.append(deck.pop())
        print("Dealer's cards after picking:", dealer_cards)

    # Recalculate player's and dealer's scores
    player_score = score_calculations(player_cards)
    dealer_score = score_calculations(dealer_cards)
    
    # Determine the winner
    if player_score > 21:
        print("Bust! You lost the game.")
    elif dealer_score > 21 or dealer_score < player_score:
        print("Player won the match.")
    elif dealer_score > player_score:
        print("Dealer won the game.")
    else:
        print("It's a draw.")

# Main part of the program
deck = deck_creation()
random.shuffle(deck)
player_cards = dealing_cards(deck)
dealer_cards = dealing_cards(deck)
print("Welcome to Mini-Blackjack!")
game_logic(player_cards, dealer_cards, deck)
