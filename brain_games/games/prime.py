from brain_games.functions import begin, is_prime, quest
from random import randint
import prompt


def game():
    begin(test_prime_numbers, 'prime')


# Функция проверки на простату
def test_prime_numbers():
    random_number = randint(1, 100)
    quest(random_number)
    user_answer = prompt.string('Your answer: ')
    counter_number = is_prime(random_number)
    if random_number == counter_number:
        currect_answer = 'yes'
    else:
        currect_answer = 'no'
    return user_answer, currect_answer
