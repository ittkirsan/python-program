# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

number = int(input('Введите число: '))
print()

for row in range(1, number + 1):
    for col in range(1, number + 1):
        if col <= row:
            print(row, end='\t')

    print()
