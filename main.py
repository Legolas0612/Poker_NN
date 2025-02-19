import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

class Card:
    def __init__(self, sign, value):
        self.sign = sign
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.sign}"

class Deck:
    def __init__(self):
        self.signs = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(sign, value) for sign in self.signs for value in self.values]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

def get_card_value(card):
    value_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return value_order[card.value]

def determine_winner(player_hand, community_cards):
    all_cards = player_hand + community_cards
    highest_card = max(all_cards, key=get_card_value)
    return highest_card

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
    winning_card = determine_winner(player.hand, community_cards)
    print(f"\nWinning card: {winning_card}")

if __name__ == "__main__":
    main()


