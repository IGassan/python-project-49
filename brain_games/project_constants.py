import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def number():
    return randint(1, 100)

def answer():
    answer_is = prompt.string('Your answer: ')
    return answer_is