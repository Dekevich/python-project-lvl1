import random

from brain_games.game_engine import run_game


def generate_random_expr(max_num=100):
    operands = ('+', '-', '*')
    number1 = random.randint(0, max_num)
    number2 = random.randint(0, max_num)
    operand = random.choice(operands)
    return '{0} {1} {2}'.format(number1, operand, number2)


def calculate_expr(expression):
    return str(eval(expression))  # noqa: S307


def main():
    description = 'What is the result of the expression?'
    run_game(description, generate_random_expr, calculate_expr)


if __name__ == '__main__':
    main()
