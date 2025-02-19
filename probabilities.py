from main import Card
from main import get_card_value

def chen_formula(hand):
    value1 = get_card_value(hand[0])
    value2 = get_card_value(hand[1])
    chen_value = 0
    highest_card = 0

    if value1 > value2: highest_card = value1
    elif value1 < value2: highest_card = value2
    else:
        highest_card = value1
        #implement logic same height

    if highest_card == 14: chen_value += 10
    elif highest_card >= 11: chen_value += value1 - 5
    else: chen_value += value1 / 2

    return chen_value

def main():
    hand = (Card('♥', '3'), Card('♥', '2'))
    print(chen_formula(hand))

if __name__ == "__main__":
    main()