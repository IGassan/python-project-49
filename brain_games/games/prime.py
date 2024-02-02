from random import randint


PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Функция проверки на простату
def determine_prime_number():
    random_number = randint(1, 100)
    if is_prime(random_number):
        currect_answer = 'yes'
    else:
        currect_answer = 'no'
    return currect_answer, str(random_number)


# функция проверки на простое число
def is_prime(random_number):
    counter_number = 2
    while random_number % counter_number != 0 and random_number != 1:
        counter_number += 1
    if random_number == counter_number:
        answer = True
    else:
        answer = False
    return answer
