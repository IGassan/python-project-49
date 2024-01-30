import prompt


# функция приветствия пользователя
def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# функция цикла
def counter(functin):
    for i in range(3):
        user_answer, currect_answer = functin()
        if user_answer == currect_answer:
            print('Correct!')
        else:
            return user_answer, currect_answer


# функция вывода ответа
def print_a_responce(name_user, answer):
    if answer:
        wrong, currect = answer
        print(f"'{wrong}' is wrong answer ;(. Correct answer was '{currect}'.")
        print(f"Let's try again, {name_user}!")
    else:
        print(f'Congratulations, {name_user}!')
