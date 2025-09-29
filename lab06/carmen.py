import random

from geography import countries
#importing my data from the other file in this folder!
from haversine import haversine
#importing the havesine file from the install

def random_hint(country):
    match random.choice(["capital", "region", "landmark", "distance"]):
        case "capital":
            hint = "whose capital is " + country["capital"]
        case "region":
            hint = "in " + country["region"]
        case "landmark":
            hint = "where you can find " + random.choice(country["landmarks"])
        case "distance":
            los_angeles = (34.0522, -118.2437)
            from_LA = round(haversine(los_angeles, country["coordinates"], unit="km"))
            hint = "approximately " + str(from_LA) + " km from Los Angeles"
    return "Carmen is in a country " + hint

#country_names = ["colombia", "barbados", "vanuatu", "eswatini", "bhutan", "iceland"]

#converting the keys of the country dictionary and turning them into a list
def random_country_name():
    #select a random country name from the key in the countries dictionary we imported. 
    #we have to convert the keys to a list, because random.choice() only works on lists,
    # and the keys of a dictionary are not a list in python
    return random.choice(list(countries.keys()))




current_country_name = random_country_name()
correct_count = 0
wrong_count = 0
#the actual function of the game that outputs where carmen is and if you got it right
while True:
    country = countries[current_country_name]
    print("Guess where Carmen is, or say 'hint' or 'exit'.")
    guess = input("Where are you going to look? ").strip().lower()
    #strip and lower get rid of the extra spaces and capitalization so you can be nice to your users!
    if guess == current_country_name:
        correct_count += 1
        print("She was here, but you missed her by one hour!")
        current_country_name = random_country_name()
    elif guess == "hint":
        print(random_hint(country))
    elif guess == "exit":
        print("Thank you for playing!")
        break
    elif guess in countries:
        print("Oh no, she's not here!")
        wrong_count += 1
    else:
        print("I don't know that country. :(")

    print("Correct guess count: " + str(correct_count))
    print("Correct guess count: " + str(wrong_count))