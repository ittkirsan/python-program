# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)

# ^        ^
#  ^      ^
#   ^    ^
#    ^  ^
#     ^^
#     ^^
#    ^  ^
#   ^    ^
#  ^      ^
# ^        ^


size = int(input('Введите сторону квадрата: '))

for row in range(size):
    for col in range(size):
        if row == col or col == - row + size - 1:
            print('^', end=' ')
        else:
            print(' ', end=' ')
    print()
