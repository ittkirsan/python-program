# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

number = int(input('Введите число: '))

for row in range(number):
    for col in range(number*2):
        if col <= row:
            print(number - col, end='')
        elif col >= number*2 - row-1:
            print(col + 1 - number, end='')
        else:
            print('.', end='')
    print()
