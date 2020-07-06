import math
import random

from brain_games.game_engine import greet_user, run_game, show_results


def get_two_random_numbers_string(max_num=100):
    number1 = random.randint(0, max_num)
    number2 = random.randint(0, max_num)
    return '{0} {1}'.format(number1, number2)


def calculate_gcd(numbers_string):
    num1, num2 = [int(num) for num in numbers_string.split(' ')]
    return str(math.gcd(num1, num2))


def brain_even():
    game_description = 'Find the greatest common divisor of given numbers.'
    username = greet_user(game_description)

    game_results = run_game(get_two_random_numbers_string, calculate_gcd)

    show_results(username, game_results)


def main():
    brain_even()


if __name__ == '__main__':
    main()
