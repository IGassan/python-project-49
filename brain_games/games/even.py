from brain_games.functions import quest
from random import randint
import prompt


# Функция проверки на четность
def parity_check():
    random_number = randint(1, 100)
    quest(random_number)
    user_answer = prompt.string('Your answer: ')
    if random_number % 2 == 0:
        currect_answer = 'yes'
    else:
        currect_answer = 'no'
    return user_answer, currect_answer
