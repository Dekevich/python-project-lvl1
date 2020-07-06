import random

import prompt

from brain_games.scripts.common_utils import greet_user


def main():
    description = 'Answer "yes" if number is even otherwise answer "no".'
    username = greet_user(description)

    game_data = play_game()
    display_game_outcome(username, game_data)


def play_game(score_to_win=3):
    current_score = 0

    while current_score < score_to_win:
        number = get_random_number()
        print('Question: {0}'.format(number))

        answer = prompt.string('Your answer: ').lower()
        correct_answer = 'yes' if (number % 2 == 0) else 'no'

        if player_answer_is_correct(answer, correct_answer):
            current_score += 1
            print('Correct!')
        else:
            return {
                'outcome': 'lose',
                'answer': answer,
                'correct': correct_answer,
            }

    return {'outcome': 'win'}


def get_random_number(max_num=100):
    return random.randint(0, max_num)


def player_answer_is_correct(answer, correct_answer):
    allowed_answers = ['yes', 'no']
    return answer in allowed_answers and answer == correct_answer


def display_game_outcome(username, game_data):
    game_outcome = game_data['outcome']

    if game_outcome == 'win':
        print(f'Congratulations, {username}!')
    elif game_outcome == 'lose':
        answer = game_data['answer']
        correct_answer = game_data['correct']
        template = "'{0}' is wrong answer ;(. Correct answer was '{1}'."

        print(template.format(answer, correct_answer))
        print("Let's try again, {0}!".format(username))


if __name__ == '__main__':
    main()
