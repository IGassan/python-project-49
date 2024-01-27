from brain_games.project_constants import welcome_user, number
from brain_games.project_constants import answer, answer_for_yes_no


# Функция проверки на четность
def parity_check():
    user = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        random_number = number(100)
        print(f'Question: {random_number}')
        user_ans = answer()
        if random_number % 2 == 0:
            currect_answer = 'yes'
        else:
            currect_answer = 'no'
        counter = answer_for_yes_no(user_ans, currect_answer, user, counter)
    if counter == 3:
        print(f'Congratulations, {user}!')
