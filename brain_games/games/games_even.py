from brain_games.project_constants import welcome_user
from brain_games.project_constants import counter, print_a_responce
from random import randint
import prompt


def game():
    name_user = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer = counter(parity_check)
    print_a_responce(name_user, answer)


# Функция проверки на четность
def parity_check():
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    user_answer = prompt.string('Your answer: ')
    if random_number % 2 == 0:
        currect_answer = 'yes'
    else:
        currect_answer = 'no'
    return user_answer, currect_answer
