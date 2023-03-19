# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

a, b = map(int, input('Введите два числа через пробел: ').split())

def rec_sum(a, b):
    if b == 0:
        return a
    return 1 + rec_sum(a, b - 1)

print(f'Сумма чисел {a} и {b} =', rec_sum(a, b))