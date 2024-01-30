from brain_games.project_constants import welcome_user
from brain_games.project_constants import counter, print_a_responce
from random import randint, choice
import prompt


def game():
    name_user = welcome_user()
    print('What is the result of the expression?')
    answer = counter(calculator)
    print_a_responce(name_user, answer)


# Функция калькулятор
def calculator():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    operand = choice(['+', '-', '*'])
    print(f'Question: {random_number_1} {operand} {random_number_2}')
    user_answer = int(prompt.string('Your answer: '))
    match operand:
        case '+':
            currect_answer = random_number_1 + random_number_2
        case '-':
            currect_answer = random_number_1 - random_number_2
        case '*':
            currect_answer = random_number_1 * random_number_2
    return user_answer, currect_answer
