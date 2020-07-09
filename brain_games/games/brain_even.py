import random

import prompt

START_TEXT = 'Answer "yes" if number is even otherwise answer "no".'
MAX_NUMBER = 100


def get_question_and_correct_answer():
    question = random.randint(0, MAX_NUMBER)
    corect_answer = 'yes' if is_even(question) else 'no'
    return question, corect_answer


def get_player_answer():
    return prompt.string('Your answer: ').lower()


def is_even(number):
    return number % 2 == 0
