# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
amount_numbers = int(input('Введите количество чисел: '))
max_sum = 0

for number in range(1, amount_numbers + 1):
    print('Введите', end=' ')
    print(number, 'число:', end=' ')
    number = int(input())
    summ = 0
    num = number
    while num > 0:
        summ += num % 10
        num //= 10
    if summ > max_sum:
        max_sum = summ
        max_number = number
print('Из введенных чисел', max_number,
      'имеет максимальную сумму цифр:', max_sum)
