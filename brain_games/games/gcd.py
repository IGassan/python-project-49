from random import randint


GCD = 'Find the greatest common divisor of given numbers.'


# Функция калькулятор
def determine_divisor():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    rand_number_1 = random_number_1
    rand_number_2 = random_number_2
    while random_number_1 != 0 and random_number_2 != 0:
        if random_number_1 > random_number_2:
            random_number_1 = random_number_1 % random_number_2
        else:
            random_number_2 = random_number_2 % random_number_1
    currect_answer = random_number_1 + random_number_2
    operand = str(rand_number_1) + ' ' + str(rand_number_2)
    return currect_answer, operand
