# Programmer: Estella Moody
from cards import poker_classification, deal
while True:
    num_players = (input("Enter the number of players(2-10): ")
                   ).strip().lower()
    if num_players in ("bye", "exit"):
        break

    try:
        num_players = int(num_players)
    except ValueError:
        print("Invalid input. Please enter an integer between 2 and 10.")
        continue
    if not isinstance(num_players, int):
        print("Invalid input. Please enter an integer between 2 and 10.")
        continue
    if num_players < 2 or num_players > 10:
        print("Invalid number of players. Please enter a number between 2 and 10.")
        continue

    hands = deal(num_players, 5)
    for hand in hands:
        hand_str = " ".join(sorted(str(card) for card in hand))
        classification = poker_classification(hand)
        print(f"{hand_str} is a {classification}")
