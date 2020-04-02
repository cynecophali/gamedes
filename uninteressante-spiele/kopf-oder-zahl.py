#!/usr/bin/env python3

from datetime import datetime
import logging
from random import randint

coin = {
    0: 'Kopf',
    1: 'Zahl',
}


def toss_coin():
    key = randint(0, 1)
    return (key, coin[key])


def setup_logger(filename='debug.log'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(filename)
    ch = logging.StreamHandler()

    fh.setLevel(logging.DEBUG)
    ch.setLevel(logging.INFO)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


def default_game(cash, bet, rounds):
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%dT%H.%M.%S')
    logger = setup_logger(filename=f'default_game_{timestamp}.log')
    logger.info(f'playing {rounds} rounds with {cash} cash and {bet} bets')

    for i in range(0, rounds):
        guess, guess_side = toss_coin()
        toss, toss_side = toss_coin()

        logger.debug(f'guess {guess_side}\ttoss {toss_side}')

        if guess == toss:
            cash += bet
        else:
            cash -= bet

    logger.info(f'result: {cash}')


cash = 100.0
bet = 1.0
rounds = 100

default_game(cash, bet, rounds)
