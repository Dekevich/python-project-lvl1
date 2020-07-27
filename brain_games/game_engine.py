import prompt

TOTAL_ROUNDS = 3
START_ROUND = 1
OUTCOME_LOSE = 'lose'
OUTCOME_WIN = 'win'


def run_game(game):
    start_text = game.START_TEXT
    question_getter = game.get_question_and_correct_answer
    answer_type = game.ANSWER_TYPE

    show_game_intro(start_text)
    username = get_username()
    greet_user(username)
    game_results = game_loop(question_getter, answer_type)
    show_results(username, game_results)


def show_game_intro(start_text):
    print('Welcome to the Brain Games!')
    print(start_text, end='\n\n')


def get_username():
    return prompt.string('May I have your name? ')


def greet_user(username):
    print(f'Hello, {username}!', end='\n\n')


def game_loop(question_getter, answer_type):
    current_round = START_ROUND

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
