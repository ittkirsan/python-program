# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|

frame_length = int(input('Введите длинну рамки: '))
frame_width = int(input('Введите ширину рамки: '))

for row in range(frame_width + 1):
    for col in range(frame_length + 1):
        if (col == 0 or col == frame_length):
            print('|', end='')
        elif (row == 0 or row == frame_width):
            print('-', end='')
        else:
            print(' ', end='')
    print()
