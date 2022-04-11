# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!

number = int(input('Введите число: '))
sum_factorial = 0

for num in range(1, number + 1):
    factorial_num = 1
    for num_fc in range(1, num + 1):
        factorial_num *= num_fc
    sum_factorial += factorial_num

print('Cуммa факториалов равна:', sum_factorial)
