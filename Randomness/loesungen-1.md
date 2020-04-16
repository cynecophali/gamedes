---
title: Aufgaben SW09
subtitle: Randomness
author: Maurin Donat Thalmann, Patrick Bucher, Pascal Kiser
---

# Aufgabe 1

Es gibt 36 mögliche Würfelkombinationen:

$$ 6 \cdot 6 = 36$$

Fünf davon sind Unentschieden, und fallen deshalb weg. Das Spiel hat somit 31 verschiedene mögliche Würfelkombinationen:

$$ 36 - 5 = 31 $$

Insgesamt gibt es $10$ positive und $21$ negative Kombinationen, siehe folgende Tabelle:

```
   D  2  3  4  5  6
1 -1 -1 -1 -1 -1 -1 = -6
2 -1  0 -1 -1 -1 -1 = -5
3 -1 +2  0 -1 -1 -1 = -2
4 -1 +2 +2  0 -1 -1 = +1
5 -1 +2 +2 +2  0 -1 = +4
6 -1 +2 +2 +2 +2  0 = +7
                    = -1
```

Das Spielen lohnt sich langfristig nicht.

Der erwartete Gewinn pro Runde beträgt somit:

$$ \Bigg( \frac{10}{31} \cdot  2 \Bigg) - \Bigg( \frac{21}{31} \cdot  1 \Bigg)  = -0.\overline{032258064516129} $$

Der erwartete Gewinn ist somit kleiner als der erwartete Gewinn beim _Nicht-Spielen_ ( $\approx 0$). Es sollte also _nicht_ gespielt werden.

## Simulation

```python
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
```

Ausgabe:

```
simulate 1 times: outcome=2.0
simulate 10 times: outcome=0.0
simulate 100 times: outcome=-0.07
simulate 1000 times: outcome=0.036
simulate 10000 times: outcome=-0.0271
simulate 100000 times: outcome=-0.02963
simulate 1000000 times: outcome=-0.02836
```

# Aufgabe 2

## Simulation

```python
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
```

Ausgabe:

```
simulate 1 times: outcome=-1.0
simulate 10 times: outcome=0.1
simulate 100 times: outcome=-0.35
simulate 1000 times: outcome=-0.259
simulate 10000 times: outcome=-0.19
simulate 100000 times: outcome=-0.20489
simulate 1000000 times: outcome=-0.203498
```
