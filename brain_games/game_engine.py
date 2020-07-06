import prompt


def greet_user(game_description):
    print('Welcome to the Brain Games!')
    print(game_description, end='\n\n')

    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!', end='\n\n')

    return username


def display_outcome(username, game_data):
    game_outcome = game_data['outcome']

    if game_outcome == 'win':
        print(f'Congratulations, {username}!')
    elif game_outcome == 'lose':
        answer = game_data['answer']
        correct_answer = game_data['correct']
        template = "'{0}' is wrong answer ;(. Correct answer was '{1}'."

        print(template.format(answer, correct_answer))
        print("Let's try again, {0}!".format(username))
