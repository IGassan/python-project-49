from brain_games.project_constants import welcome_user, number
from brain_games.project_constants import answer, wrong_answer


# Функция проверки на простату
def test_prime_numbers():
    name_user = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    number_of_round = 0
    while number_of_round < 3:
        random_number = number(10)
        print(f'Question: {random_number}')
        user_answer = answer()
        counter = 2
        while random_number % counter != 0:
            counter += 1
        if random_number == counter:
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
