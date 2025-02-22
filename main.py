import random
import itertools

class Table:
    def __init__(self, deck):
        self.deck = deck
        self.community_cards = []

    def turn_cards(self):
        if self.community_cards.__len__() == 0:
            self.community_cards.extend(self.deck.deal(3))
        elif self.community_cards.__len__() == 3:
            self.community_cards.extend(self.deck.deal(1))
        elif self.community_cards.__len__() == 4:
            self.community_cards.extend(self.deck.deal(1))
        else: print("something went wrong with turn cards")

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
    # Sort cards by value (begin with highes card)
    cards = sorted(cards, key=get_card_value, reverse=True)
    
    # Check for different hand types
    if is_royal_flush(cards):
        return (10, [get_card_value(card) for card in cards])
    elif is_straight_flush(cards):
        return (9, [get_card_value(card) for card in cards])
    elif is_four_of_a_kind(cards):
        return (8, [get_card_value(card) for card in cards])
    elif is_full_house(cards):
        return (7, [get_card_value(card) for card in cards])
    elif is_flush(cards):
        return (6, [get_card_value(card) for card in cards])
    elif is_straight(cards):
        return (5, [get_card_value(card) for card in cards])
    elif is_three_of_a_kind(cards):
        return (4, [get_card_value(card) for card in cards])
    elif is_two_pair(cards):
        return (3, [get_card_value(card) for card in cards])
    elif is_one_pair(cards):
        return (2, [get_card_value(card) for card in cards])
    else:
        return (1, [get_card_value(card) for card in cards[:5]])  # High card

def determine_winners(players, community_cards):
    """Determine the winner based on the best hand."""
    best_hands = []
    best_rank = (0, [])
    winners = []

    for player in players:
        all_cards = player.hand + community_cards
        for combination in itertools.combinations(all_cards, 5):
            rank = evaluate_hand(combination)
            if rank > best_rank:
                best_rank = rank
                best_hands = [combination]
                winners = [player]
            elif rank == best_rank and player not in winners:
                best_hands.append(combination)
                winners.append(player)

    return winners, best_hands

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
    if len(values) == 5 and values[-1] - values[0] == 4:
        return True
    if values == [2, 3, 4, 5, 14]:
        return True
    return False

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
    num_players = 4
    players = [Player(f"Player {i+1}") for i in range(num_players)]

    table = Table(deck)


    # Deal two cards to each player
    for player in players:
        player.hand = deck.deal(2)
        print(f"{player.name}'s hand:")
        for card in player.hand:
            print(card)
        print()

    #flop
    print("flop")
    table.turn_cards()
    for card in table.community_cards:
        print(card)
    print()

    #turn
    print("turn")
    table.turn_cards()
    for card in table.community_cards:
        print(card)
    print()

    #river
    print("river")
    table.turn_cards()
    for card in table.community_cards:
        print(card)
    print()

    # Determine the winner
    winners, winning_hands = determine_winners(players, table.community_cards)
    if len(winners) == 1:
        print("The winner is!")
    else:
        print(f"Draw detected! The {len(winners)} winners are:")
    
    for i in range(len(winners)):
        print(f"{winners[i].name} with the hand:")
        for card in winning_hands[i]:
            print(card)

if __name__ == "__main__":
    main()