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

# number = int(input('Введи трехзначное число, а среднюю цифру напиши 5, чтобы по задаче подходило ахах/'
#                    'я то думал надо среднее значение вычислять...мда '))
# if number > 999 or number < 100:
#     print('Число не трехзначное facepalm')
# else:
#     if number // 100 > 0:
#         spare = number // 100 * 100
#         number = number - spare
#         print('количество сотен в числе равно ', spare // 100)
#
#     if number // 10 > 0:
#         spare = number // 10 * 10
#         number = number - spare
#         print('Десятки в числе равны ', spare // 10)
#         print('Количество единиц', number)

# 1. Реализовать вывод информации о промежутке времени в зависимости /
# от его продолжительности duration в секундах: до минуты: <s> сек; до часа:/
# <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
#
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек


# duration = int(input('Введи количество секунд всего: '))
#
# minute = 0
# hour = 0
# day = 0
# second = 0
#
# if duration // 86400 > 0:
#     day = duration // 86400
#     duration = duration - day * 86400
#     if duration // 3600 > 0:
#         hour = duration // 3600
#         duration = duration - hour * 3600
#         if duration // 60 > 0:
#             minute = duration // 60
#             duration = duration - minute * 60
#             second = duration
#             print('day = ', day)
#             print('hour = ', hour)
#             print('minute = ', minute)
#             print('second = ', second)
#         else:
#             second = duration
#             print('day = ', day)
#             print('hour = ', hour)
#             print('minute = ', minute)
#             print('second = ', second)
#     else:
#         if duration // 60 > 0:
#             minute = duration // 60
#             duration = duration - minute * 60
#             second = duration
#             print('day = ', day)
#             print('hour = ', hour)
#             print('minute = ', minute)
#             print('second = ', second)
#         else:
#             second = duration
#             print('day = ', day)
#             print('hour = ', hour)
#             print('minute = ', minute)
#             print('second = ', second)
#
#
# elif duration // 3600 > 0:
#     hour = duration // 3600
#     duration = duration - hour * 3600
#     if duration // 60 > 0:
#         minute = duration // 60
#         duration = duration - minute * 60
#         second = duration
#         print('hour = ', hour)
#         print('minute = ', minute)
#         print('second = ', second)
#     else:
#         second = duration
#         print('hour = ', hour)
#         print('minute = ', minute)
#         print('second = ', second)
# elif duration // 60 > 0:
#     minute = duration // 60
#     duration = duration - minute * 60
#     second = duration
#     print('minute = ', minute)
#     print('second = ', second)
# else:
#     second = duration
#     print('second = ', second)

import datetime
duration= 10000000
time_format = str(datetime.timedelta(seconds = duration))
print("Time in preferred format :-",time_format)




# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.