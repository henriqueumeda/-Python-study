from random import randint
from time import sleep
print('-' * 30)
print('{:^30}'.format('LOTTERY'))
print('-' * 30)
number_of_games = int(input('How many times do you want to play? '))

game_list = []
for counter in range(1, number_of_games + 1):
    for numbers in range(0, 7):
        while True:
            number = randint(1, 60)
            if number not in game_list:
                game_list.append(number)
                break
    game_list.sort()
    print(f'Game {counter}: {game_list}')
    game_list.clear()
    sleep(1)
