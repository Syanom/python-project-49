import random

from brain_games.cli import welcome_user
from brain_games.game_engine import game

MAX_ROUNDS = 3


def generate_questions():
    questions = {}
    for _ in range(MAX_ROUNDS):
        number = random.randint(1, 100)
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        questions[number] = correct_answer
        
    return questions


def main():
    username = welcome_user()
    game(username, generate_questions())


if __name__ == '__main__':
    main()
