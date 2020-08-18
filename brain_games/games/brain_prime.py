import random

START_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100


def get_question_and_correct_answer():
    question = random.randint(0, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            return False
    return True
