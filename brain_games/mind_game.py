import prompt


NUMBER_OF_QUESTIONS = 3


# функция запуска игры
def start(game):
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user}!')
    print(game.GAME_CONDITION)
    for i in range(NUMBER_OF_QUESTIONS):
        currect_answer, operand = game.create_game_data()
        print(f'Question: {operand}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == currect_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{currect_answer}'.")
            print(f"Let's try again, {name_user}!")
            break
    else:
        print(f'Congratulations, {name_user}!')
