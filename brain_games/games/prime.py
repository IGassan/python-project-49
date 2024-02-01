from brain_games.functions import quest, is_prime
from random import randint
import prompt


# Функция проверки на простату
def test_prime_numbers():
    random_number = randint(1, 100)
    quest(random_number)
    user_answer = prompt.string('Your answer: ')
    currect_answer = is_prime(random_number)
    return user_answer, currect_answer
