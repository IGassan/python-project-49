#!/usr/bin/env python3
from brain_games.games.even import parity_check
from brain_games.functions import begin_game

def main():
    begin_game(parity_check, 'even')


if __name__ == '__main__':
    main()
