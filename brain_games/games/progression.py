from random import randint


QUESTION = 'What number is missing in the progression?'
PROGRES_LENGTH = 11


# Функция для проверки прогрессии
def asking_question():
    step = randint(1, 10)
    first = randint(1, 10)
    random_number = randint(1, 10)
    progression = [i for i in range(first, first + PROGRES_LENGTH * step, step)]
    currect_answer = progression[random_number]
    progression[random_number] = '..'
    question = ' '.join(map(str, progression))
    return currect_answer, question
