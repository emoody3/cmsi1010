from dataclasses import dataclass
from random import shuffle


@dataclass(frozen=True)
class Card:
    suit: str
    rank: int
    # data classes are super powerful because they also check your types

    def __post_init__(self):
        # post init means to do these checks after stuff has been initialized
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        '''match self.suit:
            case "S": suit_str = "♠"
            case "H": suit_str = "♥"
            case "D": suit_str = "♦"
            case _: suit_str = "♣"
        match self.rank:
            case 1: rank_str = "A"
            case 11: rank_str = "J"
            case 12: rank_str = "Q"
            case 13: rank_str = "K"
            case _: rank_str = str(self.rank)
        return f"{rank_str}{suit_str}"'''
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"


'''def standard_deck():
    #here we get the 52 card deck through the use of a double for-loop
    #start with an empty list and append each card to it
    cards = []
    for suit in ("S", "H", "D", "C"):
        for rank in range(1, 14):
            cards.append(Card(suit=suit, rank=rank))
    return cards'''

# python has a better way to do this tho, if you give the list a rule, it can create the list for you immediately


def standard_deck():
    # doing this is called a list comprehension
    return [Card(s, r)
            for s in ("SHDC")
            for r in range(1, 14)]


def shuffled_deck():
    deck = standard_deck()
    shuffle(deck)  # this method taken from the random module
    return deck


def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])


# remember that you can print lists directly!, but it will print the wrong way unless we classify the str method in the Card class
print([str(card) for card in shuffled_deck()])
print([str(card) for card in deal_one_five_card_hand()])
