#!/usr/bin/env python3

from datetime import datetime
import logging
import random

random.seed(datetime.now())

coin = {
    0: 'Head',
    1: 'Tails',
}


def toss_coin():
    key = random.randint(0, 1)
    return (key, coin[key])


def setup_logger(filename='debug.log'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    timestamp = datetime.now().strftime('%Y-%m-%dT%H.%M.%S')
    fh = logging.FileHandler(f'{timestamp}_{filename}')
    ch = logging.StreamHandler()

    fh.setLevel(logging.DEBUG)
    ch.setLevel(logging.INFO)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


def execute(gamefunc, cash, bet, rounds):
    """General game function executor."""
    logger = setup_logger(filename=f'{gamefunc.__name__}.log')
    logger.info(f'playing {gamefunc.__name__} {rounds} rounds ' +
                f'({cash} cash, {bet} bets)')
    cash = gamefunc(cash, bet, rounds, logger)
    logger.info(f'result: {cash}')
    logger.handlers = []


def default_game(cash, bet, rounds, logger):
    """Default head/tails game."""
    for i in range(0, rounds):
        guess, guess_side = toss_coin()
        toss, toss_side = toss_coin()
        logger.debug(f'guess {guess_side}\ttoss {toss_side}')
        if guess == toss:
            cash += bet
        else:
            cash -= bet
    return cash


def streak_game(cash, bet, rounds, logger):
    """
    A variant of the head/tails game with streaks.

    If the user wins, and sets again on the same side, the amount of the win
    is doubled.
    """
    streak_length = 0
    last_guess = None
    for i in range(0, rounds):
        guess, guess_side = toss_coin()
        toss, toss_side = toss_coin()
        logger.debug(f'guess {guess_side}\ttoss {toss_side}')
        if guess == toss:
            if streak_length > 0 and guess == last_guess:
                # same guess after a win: double win successfully
                cash += bet * 2 ** streak_length
            else:
                cash += bet
            streak_length += 1
        else:
            cash -= bet
            streak_length = 0
        last_guess = guess
    return cash


def punish_streak_game(cash, bet, rounds, logger):
    """
    A variant of the head/tails game with streaks.

    If the user wins, and sets again on the same side, the amount of the win
    is doubled.
    """
    streak_length = 0
    loss_length = 0
    last_guess = None
    for i in range(0, rounds):
        guess, guess_side = toss_coin()
        toss, toss_side = toss_coin()
        logger.debug(f'guess {guess_side}\ttoss {toss_side}')
        if guess == toss:
            if streak_length > 0 and guess == last_guess:
                # same guess after a win: double win successfully
                cash += bet * 2 ** streak_length
            else:
                cash += bet
            streak_length += 1
            loss_length = 0
        else:
            if loss_length > 0:
                # successice loss: double loss
                cash -= bet * 2 ** loss_length
            else:
                cash -= bet
            streak_length = 0
            loss_length += 1
        last_guess = guess
        if cash <= 0:
            logger.info(f'player went bankrupt after {i} rounds')
            return cash
    return cash


cash = 100.0
bet = 1.0
rounds = 100

for game in [default_game, streak_game, punish_streak_game]:
    execute(game, cash, bet, rounds)
