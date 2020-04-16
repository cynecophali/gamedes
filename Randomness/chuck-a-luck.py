#!/usr/bin/env python3

import random


def simulate(n=1):
    total = 0
    for i in range(n):
        outcome = 0
        number = random.randint(1, 7)
        dice = [0, 0, 0]
        for j in range(3):
            dice[j] = random.randint(1, 7)
            if dice[j] == number:
                outcome += 1
        if outcome == 0:
            outcome -= 1
        total += outcome
    return total


for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    result = simulate(i)
    outcome = result/i
    print(f'simulate {i} times: outcome={outcome}')
