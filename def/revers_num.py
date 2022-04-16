def revers_num(number):
    rev_number = 0
    while number:
        num = number % 10
        number //= 10
        rev_number *= 10
        rev_number += num
    print("Число наоборот:", rev_number)


while True:
    number = int(input('Введите число: '))
    if number == 0:
        print('Программа завершена!')
        break
    else:
        revers_num(number)
