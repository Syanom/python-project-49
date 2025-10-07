import prompt


def round(question, correct_answer):
    users_opinion = prompt.string(f'Question: {question}\nYour answer: ')

    if users_opinion == correct_answer:
        print('Correct!')
        return (True, correct_answer, users_opinion)
    else:
        return (False, correct_answer, users_opinion)


def game(username, questions):
    counter = 0
    for question, correct_answer in questions.items():
        result, answer, users_opinion = round(question, correct_answer)
        if not result:
            print(f"'{users_opinion}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            break
        counter += 1

    if counter == len(questions):
        print(f"Congratulations!, {username}!")