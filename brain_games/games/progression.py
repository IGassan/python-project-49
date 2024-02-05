from random import randint


GAME_CONDITION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 11


# Функция для проверки прогрессии
def create_game_data():
    step = randint(1, 10)
    first = randint(1, 10)
    random_number = randint(1, 10)
    progression = list(range(first, first + PROGRESSION_LENGTH * step, step))
    currect_answer = progression[random_number]
    progression[random_number] = '..'
    question = ' '.join(map(str, progression))
    return str(currect_answer), question
