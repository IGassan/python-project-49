# from brain_games.functions import quest
from random import randint, choice


QUESTION = 'What is the result of the expression?'


# Функция калькулятор
def begin_game():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    operand = choice(['+', '-', '*'])
    match operand:
        case '+':
            currect_answer = random_number_1 + random_number_2
        case '-':
            currect_answer = random_number_1 - random_number_2
        case '*':
            currect_answer = random_number_1 * random_number_2
    question = f'{random_number_1} {operand} {random_number_2}'
    return currect_answer, question
