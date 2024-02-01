#!/usr/bin/env python3
from brain_games.games.calc import calculator
from brain_games.functions import begin_game


def main():
    begin_game(calculator, 'calc')


if __name__ == '__main__':
    main()
