from random import randint


GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


# Функция проверки на четность
def create_game_data():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        currect_answer = 'yes'
    else:
        currect_answer = 'no'
    return str(currect_answer), str(random_number)
