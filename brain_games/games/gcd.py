from brain_games.functions import quest
from random import randint
import prompt


# Функция калькулятор
def gcd():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    quest(random_number_1, random_number_2)
    user_answer = int(prompt.string('Your answer: '))
    while random_number_1 != 0 and random_number_2 != 0:
        if random_number_1 > random_number_2:
            random_number_1 = random_number_1 % random_number_2
        else:
            random_number_2 = random_number_2 % random_number_1
    currect_answer = random_number_1 + random_number_2
    return user_answer, currect_answer
