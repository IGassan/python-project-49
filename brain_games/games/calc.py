from brain_games.functions import begin, quest
from random import randint, choice
import prompt


def game():
    begin(calculator, 'calc')


# Функция калькулятор
def calculator():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    operand = choice(['+', '-', '*'])
    quest(random_number_1, operand, random_number_2)
    user_answer = int(prompt.string('Your answer: '))
    match operand:
        case '+':
            currect_answer = random_number_1 + random_number_2
        case '-':
            currect_answer = random_number_1 - random_number_2
        case '*':
            currect_answer = random_number_1 * random_number_2
    return user_answer, currect_answer
