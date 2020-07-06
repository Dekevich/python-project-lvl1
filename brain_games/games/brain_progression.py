import random

from brain_games.game_engine import run_game

MISSING_ELEMENT = '..'


def generate_progression(max_num=100, prog_length=10):
    step = random.randint(1, 10)
    first_element = random.randint(0, max_num)
    last_element = first_element + step * prog_length
    missing_element_index = random.randint(0, prog_length - 1)
    progression = [
        str(element) for element in
        range(first_element, last_element + 1, step)
    ]
    progression[missing_element_index] = MISSING_ELEMENT

    return ' '.join(progression)


def find_missing_element(prog_str):
    prog = [
        int(element) if element.isdigit() else element
        for element in prog_str.split(' ')
    ]
    missing_element_index = prog.index(MISSING_ELEMENT)
    step = 1
    for idx in range(len(prog) - 1):
        if prog[idx] != MISSING_ELEMENT and prog[idx + 1] != MISSING_ELEMENT:
            step = prog[idx + 1] - prog[idx]
            break

    if missing_element_index == 0:
        return str(prog[1] - step)

    return str(prog[missing_element_index - 1] + step)


def main():
    description = 'What number is missing in the progression?'
    run_game(description, generate_progression, find_missing_element)


if __name__ == '__main__':
    main()
