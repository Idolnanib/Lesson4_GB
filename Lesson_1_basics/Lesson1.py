# my_list = [1, 'jopa', 76, 'when', 87]
#
# print(my_list[::-1])
#
# print(dir(my_list))
#
#
# for num in reversed(my_list):
#     print(num)

# Задача. Написать программу, определяющую, что число
# трёхзначное и средняя цифра равна 5.

number = int(input('Введи трехзначное число, а среднюю цифру напиши 5, чтобы по задаче подходило ахах/'
                   'я то думал надо среднее значение вычислять...мда '))
if number > 999 or number < 100:
    print('Число не трехзначное facepalm')
else:
    if number // 100 > 0:
        spare = number // 100 * 100
        number = number - spare
        print('количество сотен в числе равно ', spare // 100)

    if number // 10 > 0:
        spare = number // 10 * 10
        number = number - spare
        print('Десятки в числе равны ', spare // 10)
        print('Количество единиц', number)

