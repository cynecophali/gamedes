---
title: 'Uninteressante Spiele: Kopf oder Zahl'
author: 'Hundsköpfige (P. Bucher, P. Kiser, M. Thalmann)'
---

Das Spiel _Kopf oder Zahl_ wurde mithilfe einer Simulation ([Quellcode](https://github.com/cynecophali/gamedes/blob/master/uninteressante-spiele/kopf-oder-zahl.py)) gespielt.

## Einfache Variante

Bei der ersten Variante (Funktion `default_game`), startet der Spieler mit 100.- Cash und setzt jede Runde 1.- auf Kopf oder Zahl. Bei einem richtigen Tipp erhält er den Einsatz gutgeschrieben, andernfalls wird ihm der Einsatz abgezogen. Es werden insgesamt 100 Runden gespielt. Am Ende hat der Spieler jeweils einen ähnlichen Betrag wie zu Beginn. (Statistisch könnte man den Bereich wohl mit einer Binomialverteilung angeben.)

## Mehr Gewinn bei steigendem Risiko

Um das Spiel interessanter zu machen, wurde ein sogenannter _Winning Streak_ eingeführt (Funktion `streak_game`). Gewinnt der Spieler, und setzt er noch einmal auf die gleiche Seite, und gewinnt dabei wieder, wird der gutgeschriebene Einsatz jeweils verdoppelt. D.h. beim dritten Gewinn in Folge mit dem gleichen Tipp wird der Einsatz bereits vervierfacht, beim vierten verachtfacht, usw.

Dies hatte zum Ergebnis, das der Spieler viel höhere Gewinne hat. Er trägt ja durch die Regeländerung kein höheres Risiko, sondern hat bloss eine _Upside_. Er wird jedoch dazu verleitet, nach einem Gewinn wieder den gleichen Tipp abzugeben. Der Spieler muss dadurch stärker abwägen.

## Strafe nach mehrmaligem Verlieren

Mit einer Art von Strafe könnte dieses mangelnde Risiko kompensiert werden, indem man z.B. bei Negativserien ebenfalls stärkere Abzüge macht. Dies wurde so umgesetzt (Funktion `punish_streak_game`), dass sich die Verluste mit jedem verlorenen Spiel wiederum verdoppeln, egal ob der Spieler dabei wieder den gleichen Tipp abgibt wie im Spiel vorher.

Unter dem Strich trägt der Spieler somit ein grösseres Risiko. Das hat zur Folge, dass der Spieler öfters am Ende des Spiels Geld verliert, oder gar schon im Laufe des Spiels bankrott geht. Grosse Gewinne sind dennoch vereinzelt möglich ‒ und auch aufgetreten. Das Spiel ist somit einem Casino etwas ähnlicher geworden, indem Gewinne zwar möglich sind, meistens aber "die Bank" gewinnt, und der Spieler in der Regel nach dem Spiel weniger Geld hat als zuvor.

## Weiter Varianten

Das höhere Risiko könnte etwas abgeschwächt werden, indem für Verluste ein geringerer Verdoppelungsfaktor als 2 verwendet wird.

Mit der gewählten Vorgehensweise wird eher die Spielmechanik im Hinblick auf das Spielergebnis analysiert als die _User Experience_ des Spielers. Hierzu könnte man die Simulation um einen interaktiven Modus erweitern.
