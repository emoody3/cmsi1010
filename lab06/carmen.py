import random
country_names = ["colombia", "barbados", "vanuatu", "eswatini", "bhutan", "iceland"]
current_country_name = random.choice(country_names)

while True:
    print("Guess where Carmen is, or say 'hint' or 'exit'.")
    guess = input("Where are you going to look? ").strip().lower()
    if guess == current_country_name:
        print("She was here, but you missed her by one hour!")
    elif guess == "hint":
        print("Sorry, no hints yet.")
    elif guess == "exit":
        print("Thank you for playing!")
        break
    else:
        print("Oh no, she’s not here!")