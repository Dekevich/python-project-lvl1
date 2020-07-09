import math
import random

import prompt

START_TEXT = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def get_question_and_correct_answer():
    num1 = random.randint(0, MAX_NUMBER)
    num2 = random.randint(0, MAX_NUMBER)
    question = f'{num1} {num2}'
    correct_answer = calculate_gcd(num1, num2)
    return question, correct_answer


def get_player_answer():
    return prompt.integer('Your answer: ')


def calculate_gcd(num1, num2):
    return math.gcd(num1, num2)
