---
title: 'Uninteressante Spiele: Kopf oder Zahl'
author: 'Hundsköpfige (P. Bucher, P. Kiser, M. Thalmann)'
---

Das Spiel _Kopf oder Zahl_ (Münzwurf) wurde mithilfe einer Simulation ([Quellcode](https://github.com/cynecophali/gamedes/blob/master/uninteressante-spiele/kopf-oder-zahl.py)) gespielt.

Der Spieler startet mit 100.- Cash und setzt jede Runde 1.- auf Kopf oder Zahl. Bei einem richtigen Tipp erhält er den Einsatz gutgeschrieben, bei einem falschen Tipp wird ihm der Einsatz abgezogen. Es werden insgesamt 100 Runden gespielt. Am Ende hat der Spieler jeweils einen ähnlichen Betrag wie zu Beginn. (Statistisch könnte man den Bereich wohl mit einer Binomialverteilung angeben.)

Um das Spiel interessanter zu machen, wurde ein sogenannter _winning streak_ eingeführt. Gewinnt der Spieler, und setzt er noch einmal auf die gleiche Seite, und gewinnt dabei wieder, wird der gutgeschriebene Einsatz jeweils verdoppelt. D.h. beim dritten Gewinn in Folge mit dem gleichen Tipp wird der Einsatz bereits vervierfacht, beim vierten verachtfacht, usw. Dies hatte zum Ergebnis, das der Spieler viel höhere Gewinne hat. Er trägt ja durch die Regeländerung kein höheres Risiko.

Mit einer Art von Strafe könnte dieses mangelnde Risiko kompensiert werden, indem man z.B. bei Negativserien ebenfalls stärkere Abzüge macht.
