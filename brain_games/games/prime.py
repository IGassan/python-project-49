from random import randint


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Функция проверки на простату
def begin_game():
    random_number = randint(1, 100)
    if is_prime(random_number):
        currect_answer = 'yes'
    else:
        currect_answer = 'no'
    return currect_answer, str(random_number)


# функция проверки на простое число
def is_prime(random_number):
    if random_number <= 1:
        return False
    counter_number = 0
    for i in range(2, random_number // 2 + 1):
        if (random_number % i == 0):
            counter_number += 1
    if counter_number <= 0:
        answer = True
    else:
        answer = False
    return answer
