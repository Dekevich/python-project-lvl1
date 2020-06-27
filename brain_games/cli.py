import prompt


def welcome_user():
    username = prompt.string('May I have your name? ')

    print('Hello, {u}!'.format(u=username))
