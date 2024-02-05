from random import randint


GAME_CONDITION = 'Find the greatest common divisor of given numbers.'


# Функция наибольшего общего делителя
def create_game_data():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    currect_answer = gcd_number(random_number_1, random_number_2)
    question = f'{random_number_1} {random_number_2}'
    return str(currect_answer), question


# Функция высичления наибольшего общего делителя
def gcd_number(number_1, number_2):
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    currect_answer = number_1 + number_2
    return currect_answer
