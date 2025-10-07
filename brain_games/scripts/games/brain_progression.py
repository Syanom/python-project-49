import random

from brain_games.cli import welcome_user
from brain_games.game_engine import game

MAX_ROUNDS = 3
PROGRESSION_LENGTH = 10


def generate_progression(start, step, missing_part):
    progression = []
    for iterator in range(PROGRESSION_LENGTH):
        if iterator == missing_part:
            progression.append('..')
            continue
        progression.append(f'{start + step * iterator}')
    return ' '.join(progression)


def generate_questions():
    questions = {}
    for _ in range(MAX_ROUNDS):
        start = random.randint(1, 100)
        step = random.randint(1, 10)
        missing_part = random.randint(0, PROGRESSION_LENGTH - 1)
        question = generate_progression(start, step, missing_part)
        correct_answer = str(start + step * missing_part)
        questions[question] = str(correct_answer)
        
    return questions


def main():
    username = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    game(username, generate_questions())


if __name__ == '__main__':
    main()
