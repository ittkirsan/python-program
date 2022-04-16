print('Задача 6. Монетка')

# Практиканту дали задание
# найти старую металлическую монетку по заданным координатам.
#
# Металлоискатель сканирует местность вокруг пользователя
# и при обнаружении/отсутствии металла прибор отображает на экране соответствующее сообщение.
#
#
# Даны два действительных числа x и y.
# Напишите функцию, которая проверяет,
# принадлежит ли точка с координатами (x,y) заштрихованному квадрату (включая его границу).
# Если точка принадлежит квадрату,
# выведите сообщение “Монетка где-то рядом”,
# иначе выведите сообщение “Монетки в области нет”.
#
# На рисунке сетка проведена с шагом 1.
#
# P.S - Смотри рисунок на сайте :)
#         ^
#         |
#        *|*
# ========+=======>
#        *|*
#         |


def metal_detector():
    x = float(input('Введите координату х: '))
    y = float(input('Введите координату y: '))
    x_1 = y_1 = 1
    x_2 = y_2 = -1
    if (x <= x_1) and (x >= x_2) and (y <= y_1) and (y >= y_2):
        print('Монетка где-то рядом!!!')
    else:
        print('Монетки в области нет.')


metal_detector()