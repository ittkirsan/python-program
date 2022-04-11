# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

size = int(input('Введите высоту пирамидки: '))
number = 0
for row in range(1, size + 1):
    print('\t' * (size - row), end='')
    for col in range(1, row):
        print(2*number + 1, end='\t\t')
        number += 1
    print()
