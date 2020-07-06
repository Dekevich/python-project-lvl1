import prompt


def display_game_intro(game_description):
    print('Welcome to the Brain Games!')
    print(game_description)
    print()


def get_username():
    return prompt.string('May I have your name?')


def greet_user(username):
    print(f'Hello, {username}!')



