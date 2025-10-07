import random

from brain_games.cli import welcome_user
from brain_games.game_engine import game

MAX_ROUNDS = 3
OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}


def generate_questions():
    questions = {}
    for _ in range(MAX_ROUNDS):
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        operator = random.choice(list(OPERATORS.keys()))
        correct_answer = str(OPERATORS.get(operator)(first_number,
                                                     second_number))
        questions[f'{first_number} {operator} {second_number}'] = correct_answer
        
    return questions


def main():
    username = welcome_user()
    game(username, generate_questions())


if __name__ == '__main__':
    main()
