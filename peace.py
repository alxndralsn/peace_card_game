# Import necessary modules
import random
import time

DEBUG = False #if we went the testing to be without pressing enter to continue
SLEEP = 1 #we can change for the testing to go quickly

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

def play_game():
    #Preparation of the game
    time.sleep(SLEEP)
    print("Let's play the Peace card game!")
    time.sleep(SLEEP)
    print("Let's prepare the deck!")
    deck = [(rank, suit) for rank in ranks for suit in suits]
    time.sleep(SLEEP)

    print("Shuffling the deck...")
    random.shuffle(deck)
    time.sleep(SLEEP)

    print("Splitting the deck...")
    p1_hand, p2_hand = split_list(deck)
    time.sleep(SLEEP)

    print("Ready to play!")
    if not DEBUG:
        input("Press enter to continue...")
    print(" ")

    #Actual playing
    time.sleep(SLEEP)
    while len(p1_hand) > 0 and len(p2_hand) > 0:
        p1_hand, p2_hand = play_round(p1_hand, p2_hand)
        assert len(p1_hand + p2_hand) == 52 #want to make sure no cards go missing
        if not DEBUG:
            input("Press enter to continue...")
        print(" ")
    
    #One of the players doesn't have any cards left
    #End of the game
    time.sleep(SLEEP)
    print("It seems one player doesn't have any cards left :'(")
    time.sleep(SLEEP)
    print("The game is over...")
    time.sleep(SLEEP)
    print("But wait!")
    time.sleep(SLEEP)
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
    time.sleep(SLEEP)
    print(f"Player 2's card is... {p2_card}")
    time.sleep(SLEEP)
    if card_comparison(p1_card, p2_card) == 0:
        print("A war has been declared!")
        time.sleep(SLEEP)
        p1_hand, p2_hand, _ = war(p1_hand, p2_hand, p1_card, p2_card)
    elif card_comparison(p1_card, p2_card) == 1:
        print("Player 1 has won this round!")
        p1_hand.extend([p1_card, p2_card])
    elif card_comparison(p1_card, p2_card) == 2:
        print("Player 2 has won this round!")
        p2_hand.extend([p1_card, p2_card])
    time.sleep(SLEEP)
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
    time.sleep(SLEEP)
    #Player 1 plays
    if len(p1_hand) >= 4: #player has enough for war
        print("Player 1 is putting down 3 cards...")
        p1_3_down = [p1_hand.pop(0), p1_hand.pop(0), p1_hand.pop(0)]
        p1_new_card = p1_hand.pop(0)
    elif 0 < len(p1_hand) < 4: #player has complications with the war
        print("Player 1 doesn't have enough cards and lacks the cardpower to fight at full force!")
        print("They shall play with what they have!")
        p1_new_card = p1_hand.pop()
        p1_3_down = p1_hand.copy()
        p1_hand = []
    elif len(p1_hand) == 0:
        print("Player 1 has 1 card left and will play it!")
        p1_new_card = p1_card
        p1_card = None
        p1_3_down = []

    #Player 2 plays
    if len(p2_hand) >= 4:
        print("Player 2 is putting down 3 cards...")
        p2_3_down = [p2_hand.pop(0), p2_hand.pop(0), p2_hand.pop(0)]
        p2_new_card = p2_hand.pop(0)
    elif 0 < len(p2_hand) < 4:
        print("Player 2 doesn't have enough cards and lacks the cardpower to fight at full force!")
        print("They shall play with what they have!")
        p2_new_card = p2_hand.pop()
        p2_3_down = p2_hand.copy()
        p2_hand = []
    elif len(p2_hand) == 0:
        print("Player 2 has 1 card left and will play it!")
        p2_new_card = p2_card
        p2_card = None
        p2_3_down = []

    print("Let's see who is going to win this war...")
    time.sleep(SLEEP)
    print(f"Player 1's card is... {p1_new_card}")
    time.sleep(SLEEP)
    print(f"Player 2's card is... {p2_new_card}")
    time.sleep(SLEEP)
    if card_comparison(p1_new_card, p2_new_card) == 0:
        print("Another war has been declared!")
        time.sleep(SLEEP)
        p1_hand, p2_hand, winner = war(p1_hand, p2_hand, p1_new_card, p2_new_card)
        if winner == 1: #we want to know the winner because we already added the new cards, not the old
            p1_hand.extend([p1_card, p2_card] + p1_3_down + p2_3_down) #we assume the order of how the cards are extended doesn't matter
        elif winner == 2:
            p2_hand.extend([p1_card, p2_card] + p1_3_down + p2_3_down)
    elif card_comparison(p1_new_card, p2_new_card) == 1:
        print("Player 1 has won this war!")
        p1_hand.extend([p1_card, p2_card, p1_new_card, p2_new_card] + p1_3_down + p2_3_down)
        winner = 1
    elif card_comparison(p1_new_card, p2_new_card) == 2:
        print("Player 2 has won this war!")
        p2_hand.extend([p1_card, p2_card, p1_new_card, p2_new_card] + p1_3_down + p2_3_down)
        winner = 2
    return (p1_hand, p2_hand, winner)

# Call the main function to start the game
play_game()
