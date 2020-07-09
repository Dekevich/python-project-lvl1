import prompt

TOTAL_ROUNDS = 3
START_ROUND = 1
OUTCOME_LOSE = 'lose'
OUTCOME_WIN = 'win'


def run_game(game):
    start_text = game.START_TEXT
    question_getter = game.get_question_and_correct_answer
    player_answer_getter = game.get_player_answer

    username = greet_user(start_text)
    game_results = game_loop(question_getter, player_answer_getter)
    show_results(username, game_results)


def greet_user(game_description):
    print('Welcome to the Brain Games!')
    print(game_description, end='\n\n')

    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!', end='\n\n')

    return username


def game_loop(question_getter, player_answer_getter):
    current_round = START_ROUND

    while current_round <= TOTAL_ROUNDS:
        question, correct_answer = question_getter()
        print(f'Question: {question}')

        player_answer = player_answer_getter()

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


def show_results(username, game_data):
    game_outcome = game_data['outcome']

    if game_outcome == OUTCOME_WIN:
        print(f'Congratulations, {username}!')
    elif game_outcome == OUTCOME_LOSE:
        answer = game_data['player_answer']
        correct = game_data['correct_answer']
        print(
            f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.",
        )
        print("Let's try again, {0}!".format(username))
