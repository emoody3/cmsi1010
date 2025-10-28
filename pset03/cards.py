from dataclasses import dataclass
from random import shuffle


@dataclass(frozen=True)
class Card:
    suit: str
    rank: int

    def __post_init__(self):
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"


def standard_deck():
    return [Card(suit, rank) for suit in "SHDC" for rank in range(1, 14)]


def shuffled_deck():
    cards = standard_deck()
    shuffle(cards)
    return cards


def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])

# Programmer: Estella Moody


def deal(number_of_hands, cards_per_hand):
    if number_of_hands < 1:
        raise ValueError("number_of_hands must be at least 1")
    if not (isinstance(number_of_hands, int)):
        raise TypeError("number_of_hands must be an integer")
    if not (isinstance(cards_per_hand, int)):
        raise TypeError("cards_per_hand must be an integer")
    if cards_per_hand < 1:
        raise ValueError("cards_per_hand must be at least 1")
    if cards_per_hand * number_of_hands > 52:
        raise ValueError("Not enough cards in the deck to deal")

    hands = []
    deck = shuffled_deck()
    for _ in range(number_of_hands):
        hand = set(card for card in deck[:cards_per_hand])
        hands.append(hand)
        deck = deck[cards_per_hand:]
    return hands


def poker_classification(hand):
    # raises errors if not correct input
    if not isinstance(hand, set):
        raise TypeError("hand must be a set of Card objects")
    if len(hand) != 5:
        raise ValueError("hand must contain exactly 5 cards")

    ranks = sorted([card.rank for card in hand])
    suits = [card.suit for card in hand]
    rank_counts = [ranks.count(rank) for rank in set(ranks)]
    # validates that an ace can be high or low in a straight
    if set(ranks) == {1, 10, 11, 12, 13}:
        is_straight = True
    else:
        is_straight = all(ranks[i] + 1 == ranks[i + 1] for i in range(4))

    is_flush = len(set(suits)) == 1
    is_four_kind = 4 in rank_counts
    is_full_house = sorted(rank_counts) == [2, 3]
    is_three_kind = 3 in rank_counts and not is_full_house
    is_two_pair = rank_counts.count(2) == 2
    is_one_pair = rank_counts.count(2) == 1

    # tests for the different poker hands in order of rank
    if is_straight and is_flush:
        if set(ranks) == {1, 10, 11, 12, 13}:
            return "Royal Flush"
        return "Straight Flush"
    elif is_four_kind:
        return "Four of a Kind"
    elif is_full_house:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif is_three_kind:
        return "Three of a Kind"
    elif is_two_pair:
        return "Two Pair"
    elif is_one_pair:
        return "One Pair"
    else:
        return "High Card"
