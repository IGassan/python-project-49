from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


# Функция проверки на четность
def begin_game():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        currect_answer = 'yes'
    else:
        currect_answer = 'no'
    return currect_answer, str(random_number)
