#!/usr/bin/env python3
from brain_games.games.calc import calculate, CALC
from brain_games.functions import start_game


def main():
    start_game(CALC, calculate)


if __name__ == '__main__':
    main()
