import math
import random

START_TEXT = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def get_question_and_correct_answer():
    num1 = random.randint(0, MAX_NUMBER)
    num2 = random.randint(0, MAX_NUMBER)
    question = f'{num1} {num2}'
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer
