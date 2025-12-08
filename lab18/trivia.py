from urllib.parse import unquote
import requests
import random
# if you create an API, people can request data from it for their own coding purposes


def fetch_questions(count):
    url = f"https://opentdb.com/api.php?amount={count}&type=multiple&encode=url3986"
    response = requests.get(url, timeout=15)
    # make sure you have a timeout so your program doesn't hang forever waiting for a response (assuming something is wrong)
    if response.status_code != 200:
        raise ValueError(f'API error: {response.status_code}')
    return response.json()


def check_response(body):
    if body['response_code'] != 0:
        raise ValueError(f'OpenTDB error: {body["response_code"]}')


def extract_question(body):
    question = body['results'][0]
    question['category'] = unquote(question['category'])
    question['question'] = unquote(question['question'])
    question['correct_answer'] = unquote(question['correct_answer'])
    question['incorrect_answers'] = [
        unquote(ans) for ans in question['incorrect_answers']]
    return question

# prints all the answers, and assigns letters to each answer in a dictionary that allows the game to later detecti if the user input is correct


def print_question(question):
    print(f"Category: {question['category']}")
    print(f"Question: {question['question']}")
    options = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(options)
    for i, option in enumerate(options, 1):
        print(f"{letter[i-1]}. {option}")
    global answer_pairs
    for value in options:
        answer_pairs[value] = letter[options.index(value)]

    # print(answer_pairs)
    # print(question['correct_answer'])


answer_pairs = {}
letter = ["A", "B", "C", "D"]


def play_game():
    body = fetch_questions(1)
    check_response(body)
    question = extract_question(body)
    print_question(question)
    guess = input("Your answer (A, B, C, D): ").strip().upper()
    if guess == answer_pairs[question['correct_answer']]:
        print("Correct!")
    if guess not in letter:
        raise ValueError("Invalid answer choice.")
    else:
        print(
            f"Wrong! The correct answer was {answer_pairs[question['correct_answer']]}.")


play_game()

# the unquote function comes from python and gets rid of url encoding
