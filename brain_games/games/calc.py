# from brain_games.functions import quest
from random import randint, choice


CALC = 'What is the result of the expression?'


# Функция калькулятор
def calculate():
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
    operand = str(random_number_1) + operand + str(random_number_2)
    return currect_answer, operand
