from brain_games.project_constants import welcome_user, number
from brain_games.project_constants import answer, answer_for_yes_no


# Функция проверки на простату
def test_prime_numbers():
    user = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter < 3:
        random_number = number(100)
        print(f'Question: {random_number}')
        user_ans = answer()
        counter_number = 2
        while random_number % counter_number != 0 and random_number != 1:
            counter_number += 1
        if random_number == counter_number:
            currect_answer = 'yes'
        else:
            currect_answer = 'no'
        counter = answer_for_yes_no(user_ans, currect_answer, user, counter)
    if counter == 3:
        print(f'Congratulations, {user}!')
