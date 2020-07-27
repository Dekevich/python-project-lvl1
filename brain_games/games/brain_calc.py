import random
from operator import add, mul, sub

START_TEXT = 'What is the result of the expression?'
MAX_NUMBER = 100
ANSWER_TYPE = int


def get_question_and_correct_answer():
    question = generate_random_expression()
    correct_answer = calculate_expr(question)
    return question, correct_answer


def generate_random_expression():
    supported_operations = ('+', '-', '*')
    number1 = random.randint(0, MAX_NUMBER)
    number2 = random.randint(0, MAX_NUMBER)
    operation = random.choice(supported_operations)
    return f'{number1} {operation} {number2}'


def calculate_expr(expression):
    calc_functions = {
        '+': add,
        '-': sub,
        '*': mul,
    }

    number1, operation, number2 = expression.split(' ')

    return calc_functions[operation](int(number1), int(number2))
