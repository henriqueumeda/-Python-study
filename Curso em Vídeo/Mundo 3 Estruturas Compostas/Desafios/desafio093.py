# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:47:57 2021

@author: Issamu Umeda
"""
player = {}
gols = []
total_gols = 0
player['name'] = input('Player name: ')
number_of_matches = int(input('How many matches did {} play? '.format(player['name'])))
for match in range(0, number_of_matches):
    number_of_gols = int(input('How many gols in match {}? '.format(match)))
    gols.append(number_of_gols)
    total_gols += number_of_gols
player['gols'] = gols[:]
player['total'] = total_gols
print('-='*15)
print(player)
print('-='*15)
for keys, values in player.items():
    print('The field {} has the value of {}'.format(keys, values))
print('-='*15)
print('The player {} played {} matches.'.format(player['name'], len(gols)))
for counter in range(len(gols)):
    print('   => In match {}, did {} gols.'.format(counter, gols[counter]))
print('It was a total of {} gols.'.format(total_gols))
