# Напишите программу,
# которая считает количество простых чисел в заданной последовательности
# и выводит ответ на экран.
amount_numbers = int(input('Введите кол-во чисел в последовательности: '))
numbers = 0
for num in range(1, amount_numbers + 1):
    print('Введите', end=' ')
    print(num, 'число: ', end='')
    number = int(input())
    # простое число делется на себя и единицу
    for calculations in range(2, number):
        if number % calculations == 0:
            break
    else:
        numbers += 1
print('Простых чисел в последовательности:', numbers)
