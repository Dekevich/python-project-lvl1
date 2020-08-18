import prompt

TOTAL_ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    print(game.START_TEXT, end='\n\n')

    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!', end='\n\n')

    for _round in range(TOTAL_ROUNDS):  # noqa: WPS122
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')

        player_answer = prompt.string('Your answer: ')

        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {username}!")
            return

    print(f'Congratulations, {username}!')
