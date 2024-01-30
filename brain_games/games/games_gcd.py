from brain_games.project_constants import welcome_user
from brain_games.project_constants import counter, print_a_responce
from random import randint
import prompt


def game():
    name_user = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    answer = counter(gcd)
    print_a_responce(name_user, answer)


# Функция калькулятор
def gcd():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    print(f'Question: {random_number_1} {random_number_2}')
    user_answer = int(prompt.string('Your answer: '))
    while random_number_1 != 0 and random_number_2 != 0:
        if random_number_1 > random_number_2:
            random_number_1 = random_number_1 % random_number_2
        else:
            random_number_2 = random_number_2 % random_number_1
    currect_answer = random_number_1 + random_number_2
    return user_answer, currect_answer
