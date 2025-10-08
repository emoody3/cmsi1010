import random
words = {
    "noun": ["dog", "carrot", "chair", "toy", "rice cake", "potato", "sunglasses", "tricycle"],
    "verb": ["ran", "barked", "squeaked", "flew", "fell", "whistled", "cried", "called"],
    "adjective": ["small", "great", "fuzzy", "funny", "light", "ugly", "beautiful", "difficult"],
    "preposition": ["through", "over", "under", "beyond", "across"],
    "adverb": ["barely", "mostly", "easily", "already", "just", "quickly", "almost"],
    "color": ["pink", "blue", "mauve", "red", "transparent", "clear", "turqouise", "lavender"],
    "greeting": ["yo", "hello", "greetings", "what's up", "hey"]
}

template = ["""
    Yesterday the color noun
    verb preposition the coach’s
    adjective color noun that was
    adverb adjective before
    """, """greeting today the color noun 
    verb preposition my mother's 
    adjective color noun that happened to
    adverb verb yesterday"""]


def random_sentence():
    sentence = []
    for token in random.choice(template).split():
        if token in words:
            sentence.append(random.choice(words[token]))
        else:
            sentence.append(token)
    return " ".join(sentence) + "."


for _ in range(5):
    print(random_sentence())
