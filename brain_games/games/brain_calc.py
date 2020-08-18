import random
from operator import add, mul, sub

START_TEXT = 'What is the result of the expression?'
MAX_NUMBER = 100


def get_question_and_correct_answer():
    question = generate_random_expression()
    correct_answer = str(evaluate(parse(question)))
    return question, correct_answer


def generate_random_expression():
    supported_operations = ('+', '-', '*')
    number1 = random.randint(0, MAX_NUMBER)
    number2 = random.randint(0, MAX_NUMBER)
    operation = random.choice(supported_operations)
    return f'{number1} {operation} {number2}'


def parse(expr_string):
    number1, operation, number2 = expr_string.split(' ')
    return int(number1), operation, int(number2)


def evaluate(expression_elements):
    number1, operation, number2 = expression_elements
    calc_functions = {
        '+': add,
        '-': sub,
        '*': mul,
    }

    return calc_functions[operation](number1, number2)
