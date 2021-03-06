print('Задача 7. Ход конём')

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.
print('Введите местоположение коня: ')
horse_x = float(input('x = '))
horse_y = float(input('y = '))
horse_x, horse_y = int(horse_x * 10), int(horse_y * 10)
print()

print('Введите местоположение точки на доске: ')
point_x = float(input('x = '))
point_y = float(input('y = '))
point_x, point_y = int(point_x * 10), int(point_y * 10)

while (point_x < 0) or (7 < point_x) or (point_y < 0) or (7 < point_y):

    print('Вы не верно указали координату. Попробуйте еще раз!')
    point_x = float(input('x = '))
    point_y = float(input('y = '))
    point_x, point_y = int(point_x * 10), int(point_y * 10)

print('Конь в клетке (' + str(horse_x) + ', ' + str(horse_y) +
      '). Точка в клетке (' + str(point_x) + ', ' + str(point_y) + ')')

if (abs(horse_x - point_x) == 2 and abs(horse_y - point_y) == 1) or (abs(horse_x - point_x) == 1 and abs(horse_y - point_y)) == 2:
    print('Да, конь может ходить в эту точку.')
else:
    print('Конь не может ходить в эту точку.')
