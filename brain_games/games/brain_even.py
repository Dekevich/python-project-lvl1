import random

from brain_games.game_engine import greet_user, run_game, show_results


def get_random_number(max_num=100):
    return random.randint(0, max_num)


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def brain_even():
    game_description = 'Answer "yes" if number is even otherwise answer "no".'
    username = greet_user(game_description)

    game_results = run_game(get_random_number, is_even)

    show_results(username, game_results)


def main():
    brain_even()


if __name__ == '__main__':
    main()
