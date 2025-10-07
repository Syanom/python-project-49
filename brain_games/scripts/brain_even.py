import random

import prompt

from brain_games.cli import welcome_user

MAX_ROUNDS = 3


def even_round():
    number = random.randint(1, 100)
    users_opinion = prompt.string(f'Question: {number}\nYour answer: ')

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    if users_opinion == correct_answer:
        print('Correct!')
        return (True, correct_answer, users_opinion)
    else:
        return (False, correct_answer, users_opinion)


def even_game(username):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < MAX_ROUNDS:
        round_result, correct_answer, users_opinion = even_round()
        if round_result:
            counter += 1
        else:
            print(f"'{users_opinion}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {username}!")
            break

    if counter == MAX_ROUNDS:
        print(f'Congratulations, {username}!')


def main():
    username = welcome_user()
    even_game(username)


if __name__ == '__main__':
    main()
