# ----------------------------------------------------------------------
# Prorgammer: Estella Moody
# This is the file mad_libs.py
import random
templates = [
    {
        "text": "The :color :animal :action over the :adjective :plant", "author": "Ray Toal"
    },
    {
        "text": "The :adjective :animal :action under the :color :plant", "author": "Ray Toal"
    },
    {
        "text": "One day a(n) :adjective :noun :past_verb into the room. Everyone gasped and dropped their :plural_noun.", "author": "McKenzie Dean"
    },
    {
        "text": "I was on a date with :name, when they :past_verb their :noun", "author": "Ollie Cunningham"
    },
    {
        "text": "I was :present_verb today when I saw :name at the :place", "author": "Estella Moody"
    },
    {
        "text": "Somewhere near the :noun there was a :animal :present_verb :adverb", "author": "Estella Moody"
    },
    {
        "text": "I was at the :place when :noun lit on fire. I tried to fix it with my :noun.", "author": "Ollie Cunningham"
    },
    {
        "text": ":name went to the :adjective :place to :verb", "author": "Ray Toal"
    },
    {
        "text": "The :noun was so :adjective that :name had to buy it.", "author": "Estella Moody"
    },
    {
        "text": "Yesterday I saw a :adjective :noun eating a :color :food", "author": "Estella Moody"
    },
    {
        "text": "The :noun decided to :verb near the :noun while feeling very :adjective", "author": "Estella Moody"
    }
]

continuing = {"yes", "oui", "si", "sure", "yeah"}
ending = {"no", "nah"}


def madlibs():
    sentence = []
    template = random.choice(templates)
    text = template["text"]
    author = template["author"]
    for token in text.split():
        if token.startswith(":"):
            wordType = token[1:]
            # ^ to get rid of the colon in the template for the user input
            while True:
                inputWord = input(f"Pick a(n) {wordType}: ")
                if len(inputWord) >= 1 and len(inputWord) <= 30:
                    sentence.append(inputWord)
                    break
                else:
                    print("Please keep it between 1 and 30 characters.")
                # add a way to redo the word if its too long/short
        else:
            sentence.append(token)
    return " ".join(sentence) + "." + f"\nAuthored by: {author}\n\n\n"


while True:
    answer = (input("Would you like to play? ")).strip().lower()
    if answer in continuing:
        print(madlibs())
    elif answer in ending:
        print("Thanks for playing!")
        break
    else:
        print("I don't know that answer")
