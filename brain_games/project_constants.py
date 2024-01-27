import prompt
from random import randint, choice


# функция приветствия пользователя
def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# функция генератора случайного числа
def number(num):
    return randint(1, num)


# функция генератора случайного оператора
def operation():
    operand = ['+', '-', '*']
    return choice(operand)


# функция вывода ответа
def answer():
    answer_is = prompt.string('Your answer: ')
    return answer_is


# функция вывода неправильного ответа
def wrong_answer(wrong, currect, name):
    print(f"'{wrong}' is wrong answer ;(. Correct answer was '{currect}'.")
    print(f"Let's try again, {name}!")


# функция ответа да или нет
def answer_for_yes_no(user_answer, currect_answer, name_user, number_of_round):
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
    return number_of_round
