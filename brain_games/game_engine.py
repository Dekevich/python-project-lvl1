import prompt

TOTAL_ROUNDS = 3
OUTCOME_LOSE = 'lose'
OUTCOME_WIN = 'win'


def run_game(game):
    print('Welcome to the Brain Games!')
    print(game.START_TEXT, end='\n\n')

    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!', end='\n\n')

    game_results = main_game_loop(
        game.get_question_and_correct_answer,
        game.ANSWER_TYPE
    )
    show_results(username, game_results)


def main_game_loop(question_getter, answer_type):
    current_round = 1

    while current_round <= TOTAL_ROUNDS:
        question, correct_answer = question_getter()
        print(f'Question: {question}')

        player_answer = get_player_answer(answer_type)

        if player_answer == correct_answer:
            current_round += 1
            print('Correct!')
        else:
            return {
                'outcome': OUTCOME_LOSE,
                'player_answer': player_answer,
                'correct_answer': correct_answer,
            }

    return {'outcome': OUTCOME_WIN}


def get_player_answer(answer_type):
    answer_getters = {
        str: prompt.string,
        int: prompt.integer,
    }
    return answer_getters[answer_type]('Your answer: ')


def show_results(username, game_data):
    game_outcome = game_data['outcome']

    if game_outcome == OUTCOME_WIN:
        print(f'Congratulations, {username}!')
    elif game_outcome == OUTCOME_LOSE:
        answer = game_data['player_answer']
        correct = game_data['correct_answer']
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        print(f"Let's try again, {username}!")
