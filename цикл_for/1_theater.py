'''
Задача. Кинотеатр

Что нужно сделать
X мальчиков и Y девочек пошли в кинотеатр и купили билеты на идущие подряд места в одном ряду.
Напишите программу, которая выдаст, как нужно сесть мальчикам и девочкам, чтобы рядом с каждым
мальчиком сидела хотя бы одна девочка, а рядом с каждой девочкой — хотя бы один мальчик.

На вход подаются два числа: количество мальчиков X и количество девочек Y. В ответе выведите
какую-нибудь строку, в которой будет ровно X символов B(обозначающих мальчиков) и Y символов
G(обозначающих девочек), удовлетворяющую условию задачи. Пробелы между символами выводить не нужно.
Если рассадить мальчиков и девочек согласно условию задачи невозможно, выведите строку «Нет решения».
'''


boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))
result_str = ''
if (boys > girls * 2) or (girls > boys * 2):
    print('Нет решений!')
elif boys >= girls:
    diff = boys - girls
    for i in range(diff):
        result_str += 'BGB'
    for j in range(girls - diff):
        result_str += 'BG'
else:
    diff = girls - boys
    for i in range(diff):
        result_str += 'GBG'
    for j in range(boys - diff):
        result_str += 'GB'
print(result_str)
