from brain_games.project_constants import *


# Функция проверки на четность
def parity_check():
    name_user = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_round = 0
    while number_of_round < 3:
        random_number = number()
        print(f'Question: {random_number}')
        user_answer = answer()
        if random_number % 2 == 0:
            currect_answer = 'yes'
        else:
            currect_answer = 'no'
        if user_answer == currect_answer:
            number_of_round += 1
            print('Correct!')
        else:
            if user_answer == 'yes':
                number_of_round = 4
                wrong_answer(user_answer, 'no', name_user)
            else:
                number_of_round = 4
                wrong_answer(user_answer, 'yes', name_user)
    if number_of_round == 3:
        print(f'Congratulations, {name_user}!')
