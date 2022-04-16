print('Задача 3. Апгрейд калькулятора')

# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
#
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
#
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
#
# Напишите программу,
# которая спрашивает у пользователя число и действие,
# которое нужно с ним сделать:
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру.
#
# Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.


def summ_n(number):
    num = number
    suma = 0
    while number > 0:
        suma += number % 10
        number = number // 10
    print('Сумма чисел числа', num, 'равна', suma)


def max_number(number):
    max_num = 0
    while number:
        if number % 10 > max_num:
            max_num = number % 10
        number //= 10
    print("Максимальная цифра в числе равна: ", max_num)


def min_number(number):
    min_num = number % 10
    while number:
        if min_num >= number % 10:
            min_num = number % 10
            number //= 10
    print("Минимальная цифра в числе равна: ", min_num)


def calculator():
    print(''' Введите число и действие, которое нужно с ним сделать: 
  1 - вывести сумму его цифр,
  2 - вывести максимальную цифру
  3 - вывести минимальную цифру. ''')
    print()
    number = int(input('Число: '))
    action = int(input('Действие: '))

    if action == 1:
        summ_n(number)
    elif action == 2:
        max_number(number)
    elif action == 3:
        min_number(number)
    else:
        print('Ошибка ввода! Начните заново!')
        print()


while True:
    calculator()