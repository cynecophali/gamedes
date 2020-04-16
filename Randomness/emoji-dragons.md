---
title: Aufgaben SW09
subtitle: Randomness
author: Maurin Donat Thalmann, Patrick Bucher, Pascal Kiser
---

## Aufgabe 1

Es gibt 36 mögliche Würfelkombinationen:

$$ 6 \cdot 6 = 36$$

Fünf davon sind Unentschieden, und fallen deshalb weg. Das Spiel hat somit 31 verschiedene mögliche Würfelkombinationen:

$$ 36 - 5 = 31 $$

Insgesamt gibt es $10$ positive und $21$ negative Kombinationen (_siehe Tabelle 1_).

| H\P | 1   |  2  |  3  | 4   |  5  | 6   |
| --- | --- | --- | --- | --- | --- | --- |
| 🐲  | ☠️  | ☠️  | ☠️  | ☠️  | ☠️  | ☠️  |
|  2  | ☠️  | 🔂  | 💰  | 💰  | 💰  | 💰  |
| 3   | ☠️  | ☠️  | 🔂  | 💰  | 💰  | 💰  |
| 4   | ☠️  | ☠️  | ☠️  | 🔂  | 💰  | 💰  |
| 5   | ☠️  | ☠️  | ☠️  | ☠️  | 🔂  | 💰  |
| 6   | ☠️  | ☠️  | ☠️  | ☠️  | ☠️  | 🔂  |

_Tabelle 1: Dragon Die Matrix_

    Legende
    --------
    ☠️  : Spieler verliert
    🔂 : Unentschieden (Wiederholung)
    💰 : Spieler gewinnt

Der erwartete Gewinn pro Runde beträgt somit:

$$ \Bigg( \frac{10}{31} \cdot  2 \Bigg) - \Bigg( \frac{21}{31} \cdot  1 \Bigg)  = -0.\overline{032258064516129} $$

Der erwartete Gewinn ist somit kleiner als der erwartete Gewinn beim _Nicht-Spielen_ ( $\approx 0$). Es sollte also _nicht_ gespielt werden.
