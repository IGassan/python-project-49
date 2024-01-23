import prompt
from random import randint, choice


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def number():
    return randint(1, 100)


def operation():
    operand = ['+', '-', '*']
    return choice(operand)


def answer():
    answer_is = prompt.string('Your answer: ')
    return answer_is


def wrong_answer(wrong, currect, name):
    print(f"'{wrong}' is wrong answer ;(. Correct answer was '{currect}'.")
    print(f"Let's try again, {name}!")
