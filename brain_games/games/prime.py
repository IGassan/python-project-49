from random import randint


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Функция проверки на простату
def asking_question():
    random_number = randint(1, 100)
    if is_prime(random_number):
        currect_answer = 'yes'
    else:
        currect_answer = 'no'
    return currect_answer, str(random_number)


# функция проверки на простое число
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            return False
    else:
        return True
