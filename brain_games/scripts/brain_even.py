#!/usr/bin/env python3
from brain_games.games.even import determine_parity, EVEN
from brain_games.functions import start_game


def main():
    start_game(EVEN, determine_parity)


if __name__ == '__main__':
    main()
