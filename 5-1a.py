# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

from random import randint

print('Play with bot')
candies_sum = 120
while candies_sum > 0:
    n = int(input('it is your turn: '))
    if n > 28:
        print('No more than 28 candies per turn!')
        n = int(input('Try again: '))
    candies_sum -= n
    print(candies_sum)
    if candies_sum > 0:
        bot = randint(1, 28)
        if bot > candies_sum:
            bot = randint(1, 28)
        print(f'Bot number:{bot}')
        candies_sum -= bot
        if candies_sum > 0:
            print(candies_sum)
        else:
            print('Bot is winner!')
    else:
        print('You are winner!')


