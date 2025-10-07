import random

from brain_games.cli import welcome_user
from brain_games.game_engine import game

MAX_ROUNDS = 3


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_questions():
    questions = {}
    for _ in range(MAX_ROUNDS):
        number = random.randint(1, 50000)
        question = str(number)
        answer = 'yes' if is_prime(number) else 'no'
        questions[question] = answer
        
    return questions


def main():
    username = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game(username, generate_questions())


if __name__ == '__main__':
    main()
