import prompt


def greet_user(game_description):
    print('Welcome to the Brain Games!')
    print(game_description, end='\n\n')

    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!', end='\n\n')

    return username


def run_game(question_fn, answer_fn):
    total_rounds = 3
    current_round = 1

    while current_round <= total_rounds:
        question = question_fn()
        print('Question: {0}'.format(question))

        answer = prompt.string('Your answer: ').lower()
        correct_answer = answer_fn(question)

        if answer == correct_answer:
            current_round += 1
            print('Correct!')
        else:
            return {
                'outcome': 'lose',
                'answer': answer,
                'correct': correct_answer,
            }

    return {'outcome': 'win'}


def show_results(username, game_data):
    game_outcome = game_data['outcome']

    if game_outcome == 'win':
        print(f'Congratulations, {username}!')
    elif game_outcome == 'lose':
        answer = game_data['answer']
        correct_answer = game_data['correct']
        template = "'{0}' is wrong answer ;(. Correct answer was '{1}'."

        print(template.format(answer, correct_answer))
        print("Let's try again, {0}!".format(username))
