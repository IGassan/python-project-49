from brain_games.project_constants import number, answer
from brain_games.project_constants import welcome_user


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
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name_user}!")
            else:
                number_of_round = 4
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name_user}!")
    if number_of_round == 3:
        print(f'Congratulations, {name_user}!')
