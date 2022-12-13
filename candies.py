#  Создайте программу для игры с конфетами человек против человека.
# *' Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
from random import randint as rnd


def greet():
    """Знакомство с игроками"""
    global player_1
    global player_2
    print('Добро пожаловать в игру с конфетами!')
    player_1 = input('Введите имя 1 игрока: ')
    player_2 = input('Введите имя 2 игрока: ')
    return player_1, player_2


def toss_of_the_coin(player_1, player_2):
    """Жеребьевка"""
    toss = rnd(0, 1)
    if toss == 0:
        current_player = player_1
        print(f'{player_1} ходит первым!')
        return current_player
    else:
        current_player = player_2
        print(f'{player_2} ходит первым!')
        return current_player


bank = 117
count1 = 0
count2 = 0
greet()
current_player = toss_of_the_coin(player_1, player_2)

while True:
    if current_player == player_1:
        amount1 = int(input(f'{current_player}, введите количество конфет, которое хотите взять: '))
        if amount1 > 0 and amount1 < 29 and amount1 <= bank:
            count1 += amount1
            bank -= amount1
            print(f'{current_player} взял {amount1} конфет! У него {count1}.')
            print(f'На столе осталось {bank} конфет')
            current_player = player_2
        else:
            print('Столько взять нельзя! Введите другое число. ')
    else:
        amount2 = int(input(f'{current_player}, введите количество конфет, которое хотите взять: '))
        if amount2 > 0 and amount2 < 29 and amount2 <= bank:
            count2 += amount2
            bank -= amount2
            print(f'{current_player} взял {amount2} конфет! У него {count2}.')
            print(f'На столе осталось {bank} конфет')
            current_player = player_1
        else:
            print('Столько взять нельзя! Введите другое число. ')
    if bank < 29:
        print(f'{current_player} победил!')
        break

