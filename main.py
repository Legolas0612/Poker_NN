import random
import itertools

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

class Card:
    def __init__(self, sign, value):
        self.sign = sign
        self.value = value

    def __str__(self):
        return f"{self.value}{self.sign}"

class Deck:
    def __init__(self):
        self.signs = ['♥', '♦', '♣', '♠']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(sign, value) for sign in self.signs for value in self.values]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

def get_card_value(card):
    value_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return value_order[card.value]

def evaluate_hand(cards):
    """Evaluate the best hand from the given cards."""
    # Sort cards by value
    cards = sorted(cards, key=get_card_value, reverse=True)
    
    # Check for different hand types
    if is_royal_flush(cards):
        return (10, cards)
    elif is_straight_flush(cards):
        return (9, cards)
    elif is_four_of_a_kind(cards):
        return (8, cards)
    elif is_full_house(cards):
        return (7, cards)
    elif is_flush(cards):
        return (6, cards)
    elif is_straight(cards):
        return (5, cards)
    elif is_three_of_a_kind(cards):
        return (4, cards)
    elif is_two_pair(cards):
        return (3, cards)
    elif is_one_pair(cards):
        return (2, cards)
    else:
        return (1, cards[:5])  # High card

def determine_winner(player_hand, community_cards):
    """Determine the winner based on the best hand."""
    all_cards = player_hand + community_cards
    best_hand = None
    best_rank = (0, [])

    # Generate all possible 5-card combinations
    for combination in itertools.combinations(all_cards, 5):
        rank = evaluate_hand(list(combination))
        if rank > best_rank:
            best_rank = rank
            best_hand = combination

    return best_hand

# Helper functions to check hand types
def is_royal_flush(cards):
    return is_straight_flush(cards) and get_card_value(cards[0]) == 14

def is_straight_flush(cards):
    return is_flush(cards) and is_straight(cards)

def is_four_of_a_kind(cards):
    values = [card.value for card in cards]
    return any(values.count(value) == 4 for value in values)

def is_full_house(cards):
    values = [card.value for card in cards]
    return any(values.count(value) == 3 for value in values) and any(values.count(value) == 2 for value in values)

def is_flush(cards):
    suits = [card.sign for card in cards]
    return len(set(suits)) == 1

def is_straight(cards):
    values = sorted(set(get_card_value(card) for card in cards))
    return len(values) == 5 and values[-1] - values[0] == 4

def is_three_of_a_kind(cards):
    values = [card.value for card in cards]
    return any(values.count(value) == 3 for value in values)

def is_two_pair(cards):
    values = [card.value for card in cards]
    pairs = [value for value in values if values.count(value) == 2]
    return len(set(pairs)) == 2

def is_one_pair(cards):
    values = [card.value for card in cards]
    return any(values.count(value) == 2 for value in values)

def main():
    deck = Deck()
    player = Player("Player 1")

    # Deal two cards to the player
    player.hand = deck.deal(2)
    print(f"{player.name}'s hand:")
    for card in player.hand:
        print(card)

    # Deal the flop (3 community cards)
    flop = deck.deal(3)
    print("\nFlop:")
    for card in flop:
        print(card)

    # Deal the turn (1 community card)
    turn = deck.deal(1)
    print("\nTurn:")
    for card in turn:
        print(card)

    # Deal the river (1 community card)
    river = deck.deal(1)
    print("\nRiver:")
    for card in river:
        print(card)

    # Combine all community cards
    community_cards = flop + turn + river

    # Determine the winner
    winning_hand = determine_winner(player.hand, community_cards)
    print(f"\nWinning hand:")
    for card in winning_hand:
        print(card)

if __name__ == "__main__":
    main()