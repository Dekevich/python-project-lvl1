import prompt


def greet_user(game_description):
    print('Welcome to the Brain Games!')
    print(game_description, end='\n\n')

    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!', end='\n\n')

    return username
