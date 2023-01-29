# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"


# stroka = input('Введите текст для сжатия: ')
# data = open('file.txt', 'a')
# data.write(stroka)

# data.close()

data = open('file.txt', 'r')

stroka = data.read()
data.close()

def compression(text):
    if len(text) < 1:
        return ''
    count = 0
    result = ''
    elem = text[0]
    for element in text:
        if element == elem:
            count += 1
        else:
            result += str(count) + elem
            count = 1
            elem = element
    else:
        result += str(count) + elem
    return result

def recovery(text):
    if len(text) < 1:
        return ''
    num = ''
    result = ''
    for elem in text:
        if elem.isdigit():
            num += elem
        else:
            for i in range(int(num)):
                result += elem
            else:
                num = ''
    return result


print(f'Сжатие {stroka} в {compression(stroka)}')
print(f'Восстановаление данных обратно {recovery(compression(stroka))}')
        



