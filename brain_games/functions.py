from brain_games.constants import INSTRUCTIONS
import prompt


# функция запуска игры
def begin_game(function, instruction):
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user}!')
    print(INSTRUCTIONS[instruction])
    for i in range(3):
        user_answer, currect_answer = function()
        if user_answer == currect_answer:
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {name_user}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{currect_answer}'.")
            print(f"Let's try again, {name_user}!")
            break


# функция проверки на простое число
def is_prime(random_number):
    counter_number = 2
    while random_number % counter_number != 0 and random_number != 1:
        counter_number += 1
    if random_number == counter_number:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


# функция для вывода вопроса
def quest(*operand):
    string_operand = ' '.join(map(str, operand))
    print(f'Question: {string_operand}')
