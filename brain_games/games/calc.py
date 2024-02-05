from random import randint, choice


GAME_CONDITION = 'What is the result of the expression?'


# Функция калькулятор
def create_game_data():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    operator = choice('+-*')
    currect_answer = calc_number(random_number_1, random_number_2, operator)
    question = f'{random_number_1} {operator} {random_number_2}'
    return str(currect_answer), question


# Функция вычисления операции
def calc_number(number_1, number_2, operator):
    match operator:
        case '+':
            currect_answer = number_1 + number_2
        case '-':
            currect_answer = number_1 - number_2
        case '*':
            currect_answer = number_1 * number_2
    return currect_answer
