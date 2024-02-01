#!/usr/bin/env python3
from brain_games.games.gcd import gcd
from brain_games.functions import begin_game


def main():
    begin_game(gcd, 'gcd')


if __name__ == '__main__':
    main()
