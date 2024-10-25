# Import necessary modules
import random
import time

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

def play_game():
    #Preparation of the game
    time.sleep(1)
    print("Let's play the Peace card game!")
    time.sleep(1)
    print("Let's prepare the deck!")
    deck = [(rank, suit) for rank in ranks for suit in suits]
    time.sleep(1)

    print("Shuffling the deck...")
    random.shuffle(deck)
    time.sleep(1)

    print("Splitting the deck...")
    p1_hand, p2_hand = split_list(deck)
    time.sleep(1)

    print("Ready to play!")
    input("Press enter to continue...")
    print(" ")

    #Actual playing
    time.sleep(1)
    while len(p1_hand) > 0 or len(p2_hand) > 0:
        p1_hand, p2_hand = play_round(p1_hand, p2_hand)
        input("Press enter to continue...")
        print(" ")
    
    #One of the players doesn't have any cards left
    #End of the game
    time.sleep(1)
    print("It seems one player doesn't have any cards left :'(")
    time.sleep(1)
    print("The game is over...")
    time.sleep(0.5)
    print("But wait!")
    time.sleep(1)
    print("Let's see who the winner is...")

    if len(p1_hand) == 0:
        print("Player 2 has won the game!")
    elif len(p2_hand) == 0:
        print("Player 1 has won the game!")

# Split the deck into two hands
def split_list(list):
    half = len(list)//2
    return list[:half], list[half:]

def play_round(p1_hand, p2_hand):
    """
    Play a single round of the game.
	That is, each player flips a card, and the winner is determined using the card_comparison function 
    if both players flip the same value card, call the war function
	"""
    p1_card = p1_hand.pop(0)
    p2_card = p2_hand.pop(0)
    print(f"Player 1's card is... {p1_card}")
    time.sleep(1)
    print(f"Player 2's card is... {p2_card}")
    time.sleep(1)
    if card_comparison(p1_card, p2_card) == 0:
        print("A war has been declared!")
        time.sleep(1)
        p1_hand, p2_hand = war(p1_hand, p2_hand, p1_card, p2_card)
    elif card_comparison(p1_card, p2_card) == 1:
        print("Player 1 has won this round!")
        p1_hand.extend([p1_card, p2_card])
    elif card_comparison(p1_card, p2_card) == 2:
        print("Player 2 has won this round!")
        p2_hand.extend([p1_card, p2_card])
    time.sleep(1)
    print(f"Player 1 now has {len(p1_hand)} cards")
    print(f"Player 2 now has {len(p2_hand)} cards")
    return (p1_hand, p2_hand)

def card_comparison(p1_card, p2_card):
    """
    This is the logic that compares two cards to find the stronger card
    Return 1 if player 1's card is strong, 2 for player 2
    if the cards are equal, return 0.

    Hint, using the index function will make this very simple (one liner)
    """
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
        return 1
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        return 2
    else:
        return 0

def war(p1_hand, p2_hand, p1_card, p2_card):
    """
    Handle the 'war' scenario when cards are equal.
	recall the rules of war, both players put 3 cards face down, 
	then both players flip face up a 4th card. The player with the stronger
	card takes all the cards.		
	"""
    time.sleep(1)
    if len(p1_hand) >= 4 and len(p2_hand) >= 4:
        print("Player 1 and Player 2 are putting down 3 cards...")
        p1_3_down = [p1_hand.pop(0), p1_hand.pop(0), p1_hand.pop(0)]
        p2_3_down = [p2_hand.pop(0), p2_hand.pop(0), p2_hand.pop(0)]
        p1_new_card = p1_hand.pop(0)
        p2_new_card = p2_hand.pop(0)
    elif len(p1_hand) < 4:
        print("It seems Player 1 doesn't have enough cards and lacks the cardpower to fight at full force!")
        print("They shall play with what they have!")
        p1_new_card = p1_hand.pop()
        p1_3_down = p1_hand.copy
        p2_3_down = [p2_hand.pop(0), p2_hand.pop(0), p2_hand.pop(0)]
        p2_new_card = p2_hand.pop(0)
    elif len(p2_hand) < 4:
        print("It seems Player 2 doesn't have enough cards and lacks the cardpower to fight at full force!")
        print("They shall play with what they have!")
        p1_3_down = [p1_hand.pop(0), p1_hand.pop(0), p1_hand.pop(0)]
        p1_new_card = p1_hand.pop(0)
        p2_new_card = p2_hand.pop()
        p2_3_down = p2_hand.copy

    print("Let's see who is going to win this war...")
    time.sleep(1)
    print(f"Player 1's card is... {p1_new_card}")
    time.sleep(1)
    print(f"Player 2's card is... {p2_new_card}")
    time.sleep(1)
    if card_comparison(p1_new_card, p2_new_card) == 0:
        print("Another war has been declared!")
        time.sleep(1)
        p1_hand, p2_hand = war(p1_hand, p2_hand, p1_new_card, p2_new_card)
    elif card_comparison(p1_new_card, p2_new_card) == 1:
        print("Player 1 has won this war!")
        p1_hand.extend([p1_card, p2_card] + [p1_new_card, p2_new_card] + p1_3_down + p2_3_down)
    elif card_comparison(p1_new_card, p2_new_card) == 2:
        print("Player 2 has won this war!")
        p2_hand.extend([p1_card, p2_card] + [p1_new_card, p2_new_card] + p1_3_down + p2_3_down)
    return (p1_hand, p2_hand)

# Call the main function to start the game
play_game()
