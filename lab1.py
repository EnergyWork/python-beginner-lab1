import math

"""
    #1 Пять способов поменять значения переменных местами
"""
# x = int(input())
# y = int(input())

# # способ 1
# tmp = x
# x = y
# y = tmp
# # способ 2
# x, y = y, x
# # способ 3
# x = x + y
# y = x - y
# y = x - y
# # способ 4
# x = x ^ y
# y = x ^ y
# x = x ^ y
# # способ 5
# tmp = [x, y]
# x = tmp[1]
# y = tmp[0]

"""
    #2 Определить четверть
"""
# x = int(input())
# y = int(input())

# if x == 0:
#     if y == 0:
#         print('начало')
#     else:
#         print('Ox')
# elif y == 0:
#     print('Oy')
# elif x > 0:
#     if y > 0:
#         print(1)
#     else:
#         print(4)
# elif x < 0:
#     if y > 0:
#         print(2)
#     else:
#         print(3)

"""
    #3 Найти значение функции
"""
# x = int(input())
# if x > 0:
#     print(math.sqrt(4 * x))
# elif x < 0:
#     print(abs(x))
# else:
#     print(math.exp(1))

"""
    #4 Сумма цифр трехзначного числа
"""
# n = input()
# m = [int(x) for x in n]
# print(sum(m))


"""
    #5 Найти корни квадратного уравнени
"""
# a = int(input())
# b = int(input())
# c = int(input())
# d = b**2 - 4 * a * c
# print('дискрименант', d)

# if a == 0 and b == 0:
#     if c != 0:
#         print('корней нет')
#     else:
#         print('x = любое число')
# elif d < 0:
#     print('корней нет')
# else:
#     sqrtd = math.sqrt(d)
#     x1 = (-b - sqrtd) / (2 * a)
#     x2 = (-b + sqrtd) / (2 * a)
#     print('корни уравнений', x1, x2)

"""
    #6 Числа Фибоначчи
"""
# n = int(input())
# i = 0
# fib = [1, 1]
# while i < n - 2:
#     fib.append(fib[-1] + fib[-2])
#     i += 1
# print(fib)


"""
    #7 Все перестановки трехзначного числа
"""
n = int(input())




"""
    #8 Все трехзначные числа Армстронга
"""
# for num in range(100, 1000, 1):
#     if num == sum([int(x)**3 for x in str(num)]):
#         print(num)
