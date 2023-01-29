# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

# Создадим игровое поле


board = list(range(1, 10))
# создаём именно кортежи, так как выигрышные комбинации неизменны.
wins_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                     (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]


def board_draw():
    for i in range(3):
        print(board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3])


def inputing(X_or_0):
    while True:
        value = input('Куда поставить ' + X_or_0 + ' ')
        if not (value in '123456789'):
            print('Ошибка, повторите ввод.')
            continue  # метод возвращает выполнение цикла в начало
        value = int(value)
        if str(board[value - 1]) in 'X0':
            print('Эта клетка уже занята!')
            continue  # вернет к самому началу где while  чтобы пользователь опять ввел число
        board[value - 1] = X_or_0
        break  # выходим из цикла иначе будет бесконечно вводить значение


def check_win(board):
    wins_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)] # создаём именно кортежи, так как комбинации неизменны.
    for each in wins_combinations:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    else:
        return False


def main():
    counter = 0
    while True:
        board_draw()
        if counter % 2 == 0:
            inputing('X')
        else:
            inputing('0')
        if counter > 3:
            winner = check_win(board)
            if winner:
                board_draw()
                print(winner, 'выиграл!')
                break
        counter += 1
        if counter == 9:
            board_draw()
            print('Ничья.')
            break
main()