import random

START_TEXT = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10
MAX_START_NUMBER = 100
PLACEHOLDER = '..'


def get_question_and_correct_answer():  # noqa: WPS210
    first, last, step = get_progression_params()
    progression = generate_progression(first, last, step)

    missing_item_index = random.randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[missing_item_index])
    progression[missing_item_index] = PLACEHOLDER

    question = ' '.join(str(element) for element in progression)

    return question, correct_answer


def generate_progression(first, last, step):
    return list(range(first, last, step))


def get_progression_params():
    first = random.randint(0, MAX_START_NUMBER)
    step = random.randint(1, 10)
    last = first + step * (PROGRESSION_LENGTH - 1) + 1

    return first, last, step
