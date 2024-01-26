from brain_games.project_constants import welcome_user, number
from brain_games.project_constants import answer, wrong_answer


# Функция для проверки прогрессии
def progression():
    name_user = welcome_user()
    print('What number is missing in the progression?')
    number_of_round = 0
    while number_of_round < 3:
        arith_prog_step = number(10)
        first_number = number(10)
        random_number = number(10)
        original_progression = [first_number]
        for i in range(1, 11):
            original_progression.append(first_number + i * arith_prog_step)
        currect_answer = original_progression[random_number]
        original_progression[random_number] = '..'
        string_progression = ' '.join(map(str, original_progression))
        print('Question: ' + string_progression)
        user_answer = int(answer())
        if user_answer == currect_answer:
            number_of_round += 1
            print('Correct!')
        else:
            number_of_round = 4
            wrong_answer(user_answer, currect_answer, name_user)
    if number_of_round == 3:
        print(f'Congratulations, {name_user}!')

