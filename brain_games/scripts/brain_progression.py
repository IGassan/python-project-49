#!/usr/bin/env python3
from brain_games.games.progression import finding_missing_numbers, PROGRESSION
from brain_games.functions import start_game


def main():
    start_game(PROGRESSION, finding_missing_numbers)


if __name__ == '__main__':
    main()
