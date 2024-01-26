from brain_games.project_constants import welcome_user, number
from brain_games.project_constants import answer, wrong_answer


# Функция калькулятор
def gcd():
    name_user = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    number_of_round = 0
    while number_of_round < 3:
        random_number_1 = number(100)
        random_number_2 = number(100)
        print(f'Question: {random_number_1} {random_number_2}')
        user_answer = int(answer())
        while random_number_1 != 0 and random_number_2 != 0:
            if random_number_1 > random_number_2:
                random_number_1 = random_number_1 % random_number_2
            else:
                random_number_2 = random_number_2 % random_number_1
        currect_answer = random_number_1 + random_number_2
        if user_answer == currect_answer:
            number_of_round += 1
            print('Correct!')
        else:
            number_of_round = 4
            wrong_answer(user_answer, currect_answer, name_user)
    if number_of_round == 3:
        print(f'Congratulations, {name_user}!')
