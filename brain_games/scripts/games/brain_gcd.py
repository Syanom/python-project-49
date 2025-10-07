import random

from brain_games.cli import welcome_user
from brain_games.game_engine import game

MAX_ROUNDS = 3


def generate_questions():
    questions = {}
    for _ in range(MAX_ROUNDS):
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        question = f'{first_number} {second_number}'
        while second_number != 0:
            tmp = first_number % second_number
            first_number = second_number
            second_number = tmp
        questions[question] = str(first_number)
        
    return questions


def main():
    username = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    game(username, generate_questions())


if __name__ == '__main__':
    main()
