import random

from brain_games.game_engine import greet_user, run_game, show_results


def generate_random_expr(max_num=100):
    operands = ('+', '-', '*')
    number1 = random.randint(0, max_num)
    number2 = random.randint(0, max_num)
    operand = random.choice(operands)
    return '{0} {1} {2}'.format(number1, operand, number2)


def calculate_expr(expression):
    return str(eval(expression))  # noqa: S307


def brain_even():
    game_description = 'What is the result of the expression?'
    username = greet_user(game_description)

    game_results = run_game(generate_random_expr, calculate_expr)

    show_results(username, game_results)


def main():
    brain_even()


if __name__ == '__main__':
    main()
