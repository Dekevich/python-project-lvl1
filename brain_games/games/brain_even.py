import random

from brain_games.game_engine import run_game


def get_random_number(max_num=100):
    return random.randint(0, max_num)


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def main():
    description = 'Answer "yes" if number is even otherwise answer "no".'
    run_game(description, get_random_number, is_even)


if __name__ == '__main__':
    main()
