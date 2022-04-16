print('Задача 8. НОД')

# Напишите функцию, вычисляющую наибольший общий делитель двух чисел


def nod(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    print(f'Наибольший общий делитель равен:', num1 + num2)


num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
nod(num1, num2)
