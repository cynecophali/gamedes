#!/usr/bin/env python3

import random


def simulate(n=1):
    outcome = 0
    player_choices = [1, 2, 3, 4, 5, 6]
    house_choices = ['D', 2, 3, 4, 5, 6]
    for i in range(n):
        player = random.choice(player_choices)
        house = random.choice(house_choices)
        if house == 'D' or house > player:
            outcome -= 1
        elif player > house:
            outcome += 2
        else:
            continue  # draw
    return outcome


for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    result = simulate(i)
    outcome = result/i
    print(f'simulate {i} times: outcome={outcome}')
