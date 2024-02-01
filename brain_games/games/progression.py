from brain_games.functions import quest
from random import randint
import prompt


# Функция для проверки прогрессии
def progression():
    arith_prog_step = randint(1, 10)
    first_number = randint(1, 10)
    random_number = randint(1, 10)
    original_progression = [first_number]
    for i in range(1, 11):
        original_progression.append(first_number + i * arith_prog_step)
    currect_answer = original_progression[random_number]
    original_progression[random_number] = '..'
    string_progression = ' '.join(map(str, original_progression))
    quest(string_progression)
    user_answer = int(prompt.string('Your answer: '))
    return user_answer, currect_answer
