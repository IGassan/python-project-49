from brain_games.project_constants import welcome_user
from brain_games.project_constants import counter, print_a_responce
from random import randint
import prompt


def game():
    name_user = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    answer = counter(test_prime_numbers)
    print_a_responce(name_user, answer)


# Функция проверки на простату
def test_prime_numbers():
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    user_answer = prompt.string('Your answer: ')
    counter_number = 2
    while random_number % counter_number != 0 and random_number != 1:
        counter_number += 1
    if random_number == counter_number:
        currect_answer = 'yes'
    else:
        currect_answer = 'no'
    return user_answer, currect_answer
