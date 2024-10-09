# Import necessary modules
import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck 
shuffled_deck = random.shuffle(deck)

# Split the deck into two hands
def split_list(list):
    half = len(list)//2
    1st_hand = list[half:]
    2nd_hand = list[:half]
    return 1st_hand, 2nd_hand

def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    if p1_card[0] > p2_card[0]:
        return p1_card
    elif p1_card[0] < p2_card[0]:
        return p2_card
    else:
        return 0

def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here

def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here

def play_game():
    """Main function to run the game."""
    # Your code here

# Call the main function to start the game
play_game()
     
