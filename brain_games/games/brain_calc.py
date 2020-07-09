import random

import prompt

START_TEXT = 'What is the result of the expression?'
MAX_NUMBER = 100


def get_question_and_correct_answer():
    question = generate_random_expression()
    correct_answer = calculate_expr(question)
    return question, correct_answer


def get_player_answer():
    return prompt.integer('Your answer: ')


def generate_random_expression():
    operands = ('+', '-', '*')
    number1 = random.randint(0, MAX_NUMBER)
    number2 = random.randint(0, MAX_NUMBER)
    operand = random.choice(operands)
    return f'{number1} {operand} {number2}'


def calculate_expr(expression):
    return eval(expression)  # noqa: S307
