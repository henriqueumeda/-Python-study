# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:47:57 2021

@author: Issamu Umeda
"""
team = []
while True:
    player = {}
    gols = []
    total_gols = 0
    player['name'] = input('Player name: ')
    number_of_matches = int(input('How many matches did {} play? '.format(player['name'])))
    for match in range(0, number_of_matches):
        number_of_gols = int(input('How many gols in match {}? '.format(match+1)))
        gols.append(number_of_gols)
        total_gols += number_of_gols
    player['gols'] = gols[:]
    player['total'] = total_gols
    print('-='*20)
    team.append(player.copy())
    player.clear()
    while True:
        keep_asking = input('Do you want to continue? [Y/N] ').strip().upper()
        if keep_asking == 'Y' or keep_asking == 'N':
            break
        print('[ERROR] Invalid answer. Please answer only Y or N.')
    if keep_asking == 'N':
        break

print('-=' * 20)
print('code {:<15} {:<15} total'.format('name', 'gols'))
print('-' * 40)
for number, person in enumerate(team):
    print('{:>4} {:<15} {:<15} {:<5}'.format(number, person['name'], str(person['gols']), person['total']))
print('-' * 40)

while True:
    is_int = False
    player_chosen = input('Show the data of which player? (999 to stop) ')
    if player_chosen == '999':
        break
    while not is_int:
        try:
            player_chosen = int(player_chosen)
        except ValueError:
            player_chosen = input('[ERROR] This was not a valid input. Please insert the player code again.\nPlayer code: ')
        else:
            if player_chosen >= 0 and player_chosen < len(team):
                is_int = True
            else:
                player_chosen = input('[ERROR] This was not a valid input. Please insert the player code again.\nPlayer code: ')

    print('Info about the player {}'.format(team[player_chosen]['name']))
    for counter in range(len(team[player_chosen]['gols'])):
        print('   => In match {}, did {} gols.'.format(counter+1, team[player_chosen]['gols'][counter]))
