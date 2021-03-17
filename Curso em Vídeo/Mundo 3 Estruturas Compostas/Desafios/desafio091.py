# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:48:38 2021

@author: Issamu Umeda
"""

from random import randint
from time import sleep

player = {}
print('Values:')
for counter in range(1, 5):
    player['Player' + str(counter)] = randint(1, 6)
    print('Player{} got {} in the die'.format(counter, player.get('Player' + str(counter))))
    sleep(1)
print('{:=^30}'.format('PLAYERS RANK'))
rank = 0
for key, value in sorted(player.items(), key=lambda item: item[1], reverse=True):
    rank += 1
    print('{:^28}'.format('{} place: {} with {}.').format(rank, key, value))
    sleep(1)
