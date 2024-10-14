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
    return list[:half], list[half:]

p1_hand, p2_hand = split_list(deck)
p1_card = p1_hand.pop(0)
p2_card = p2_hand.pop(0)

def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    if ranks.index(p1_card[1]) > ranks.index(p2_card[1]):
        return 1
    elif ranks.index(p1_card[1]) < ranks.index(p2_card[1]):
        return 2
    else:
        return 0

def play_round(p1_hand, p2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    p1_card = p1_hand.pop(0)
    p2_card = p2_hand.pop(0)
    print(p1_card)
    print(p2_card)
    p1_extra = []
    p2_extra = []
    if card_comparison(p1_card, p2_card) == 0:
        war(p1_card, p2_card)
    elif card_comparison(p1_card, p2_card) == 1:
        p1_extra.append(p1_card, p2_card)
    elif card_comparison(p1_card, p2_card) == 2:
        p2_extra.append(p1_card, p2_card)

def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    p1_3_down = p1_hand.pop(0), p1_hand.pop(1), p1_hand.pop(2)
    p2_3_down = p2_hand.pop(0), p2_hand.pop(1), p2_hand.pop(2)
    play_round(p1_hand, p2_hand)
    if card_comparison(p1_card, p2_card) == 0:
        war(p1_card, p2_card)
    elif card_comparison(p1_card, p2_card) == 1:
        p1_extra.append(p1_3_down)
        p1_extra.append(p2_3_down)
    elif card_comparison(p1_card, p2_card) == 2:
        p2_extra.append(p1_3_down)
        p2_extra.append(p2_3_down)
    

def play_game():
    """Main function to run the game."""
    # Your code here

# Call the main function to start the game
play_game()
    
