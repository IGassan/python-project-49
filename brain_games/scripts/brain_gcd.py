#!/usr/bin/env python3
from brain_games.games.gcd import determine_divisor, GCD
from brain_games.functions import start_game


def main():
    start_game(GCD, determine_divisor)


if __name__ == '__main__':
    main()
