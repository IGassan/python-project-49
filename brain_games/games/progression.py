from random import randint


PROGRESSION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 11


# Функция для проверки прогрессии
def finding_missing_numbers():
    arith_prog_step = randint(1, 10)
    first_number = randint(1, 10)
    random_number = randint(1, 10)
    original_progression = [first_number]
    for i in range(1, PROGRESSION_LENGTH):
        original_progression.append(first_number + i * arith_prog_step)
    currect_answer = original_progression[random_number]
    original_progression[random_number] = '..'
    return currect_answer, ' '.join(map(str, original_progression))
