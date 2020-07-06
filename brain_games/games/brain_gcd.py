import math
import random

from brain_games.game_engine import run_game


def get_two_random_numbers_string(max_num=100):
    number1 = random.randint(0, max_num)
    number2 = random.randint(0, max_num)
    return '{0} {1}'.format(number1, number2)


def calculate_gcd(numbers_string):
    num1, num2 = [int(num) for num in numbers_string.split(' ')]
    return str(math.gcd(num1, num2))


def main():
    description = 'Find the greatest common divisor of given numbers.'
    run_game(description, get_two_random_numbers_string, calculate_gcd)


if __name__ == '__main__':
    main()
