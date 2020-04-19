#!/usr/bin/env python3

import random
import sys


def main():
    n_dices, n_sides = parse_params()
    for i in range(n_dices):
        print(random.randint(1, n_sides))


def parse_params():
    if len(sys.argv) < 2:
        print('usage: dice [n] [x]')
        print('\tn: number of dices')
        print('\tx: sides per die (default: 6)')
        sys.exit(1)

    n_dices = None
    n_sides = 6

    try:
        n_dices = int(sys.argv[1])
        if n_dices < 1:
            print(f'rolling {n_dices} is ludicrous')
            sys.exit(1)
    except ValueError:
        print(f'{sys.argv[1]} is not a number')
        sys.exit(1)

    if len(sys.argv) > 2:
        try:
            n_sides = int(sys.argv[2])
            if n_sides < 2:
                print(f'a dice with {n_sides} sides makes no sense')
                sys.exit(1)

        except ValueError:
            print(f'{sys.argv[2]} is not a number')
            sys.exit(1)

    return n_dices, n_sides


if __name__ == '__main__':
    main()
