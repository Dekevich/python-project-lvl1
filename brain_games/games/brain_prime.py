import random

from brain_games.game_engine import run_game


def get_random_number(max_num=100):
    return random.randint(0, max_num)


def is_prime(number):
    if number < 2:
        return 'no'
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            return 'no'
    return 'yes'


def main():
    descr = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(descr, get_random_number, is_prime)


if __name__ == '__main__':
    main()
