from brain_games.project_constants import welcome_user
from brain_games.project_constants import counter, print_a_responce
from random import randint
import prompt


def game():
    name_user = welcome_user()
    print('What number is missing in the progression?')
    answer = counter(progression)
    print_a_responce(name_user, answer)


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
    print('Question: ' + string_progression)
    user_answer = int(prompt.string('Your answer: '))
    return user_answer, currect_answer
