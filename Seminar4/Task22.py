# Задача 22. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# Пример:
#     11 6
#     2 4 6 8 10 12 10 8 6 4 2
#     3 6 9 12 15 18
#     -> 6 12

# from random import randint

# N = int(input('Введите количество элементов первой строки: '))
# lst_1 = [randint(1, N) for _ in range(N)]
# M = int(input('Введите количество элементов второй строки: '))
# lst_2 = [randint(1, M) for _ in range(M)]
# print(*lst_1)
# print(*lst_2)
# lst_3 = []
# for i in lst_1:
#     if i in lst_2:
#         lst_3.append(i)
# lst_3.sort()     # удалось исправить то что написано ниже, метод "sort()" просто не работает с множествами, надо было записывать так
# print(*set(lst_3))

# в 90% данный код выводит результат по возрастанию, но иногда выдает разносортицу, как это исправить я так и не догадался, 
# при добавлении метода "sort()" и написании в виде "print(*set(lst_3.sort()))" выдает ошибку.


# ------------------------------------------------------------------------------------------------
# разбор на семинаре 
# from random import randint

# N = int(input('Введите количество элементов первой строки: '))
# lst_1 = [randint(1, N) for _ in range(N)]
# M = int(input('Введите количество элементов второй строки: '))
# lst_2 = [randint(1, M) for _ in range(M)]
# print(*lst_1)
# print(*lst_2)
# lst_3 = []
# for i in lst_1:
#     if i in lst_2 and i not in lst_3:  # тут мы сразу проверяем есть число во втором списке и не записывали ли мы его уже раньше в третий
#         lst_3.append(i)
# lst_3.sort()
# print(*lst_3)


# ------------------------------------------------------------------------------------------------
# еще одно решение

# from random import randint
# N = int(input('Введите количество элементов первой строки: '))
# lst_1 = [randint(1, N) for _ in range(N)]
# M = int(input('Введите количество элементов второй строки: '))
# lst_2 = [randint(1, M) for _ in range(M)]
# print(*lst_1)
# print(*lst_2)
# # дальше чувак замутил какой то так называемый каскадный генератор, прочитать и понять мне его пока проблематично
# lst_3 = set(i for i in lst_1 for j in lst_2 if i in lst_2) # заполняем множество с помощью генератора, отчеивая дубли
# print(*lst_3)

# ------------------------------------------------------------------------------------------------
# еще одно решение

from random import randint
N = int(input('Введите количество элементов первой строки: '))
lst_1 = [randint(1, N) for _ in range(N)]
M = int(input('Введите количество элементов второй строки: '))
lst_2 = [randint(1, M) for _ in range(M)]
print(*lst_1)
print(*lst_2)
# решение через амперсант "&", аператор амперсант ищет пересечение двух множеств
result = sorted(set(lst_1) & set(lst_2))  # функция "sorted" сортирует элементы множества
print(*result)
