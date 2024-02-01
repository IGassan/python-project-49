#!/usr/bin/env python3
from brain_games.games.prime import test_prime_numbers
from brain_games.functions import begin_game


def main():
    begin_game(test_prime_numbers, 'prime')


if __name__ == '__main__':
    main()
