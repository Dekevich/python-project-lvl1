import random

import prompt

START_TEXT = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10
MAX_START_NUMBER = 100
PLACEHOLDER = '..'


def get_question_and_correct_answer():
    progression = generate_progression()
    missing_item_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[missing_item_index]
    progression[missing_item_index] = PLACEHOLDER
    question = ' '.join(str(element) for element in progression)

    return question, correct_answer


def get_player_answer():
    return prompt.integer('Your answer: ')


def generate_progression():
    first = random.randint(0, MAX_START_NUMBER)
    step = random.randint(1, 10)
    last = first + step * (PROGRESSION_LENGTH - 1) + 1
    return list(range(first, last, step))
