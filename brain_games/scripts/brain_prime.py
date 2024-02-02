#!/usr/bin/env python3
from brain_games.games.prime import determine_prime_number, PRIME
from brain_games.functions import start_game


def main():
    start_game(PRIME, determine_prime_number)


if __name__ == '__main__':
    main()
