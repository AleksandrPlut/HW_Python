# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

n = int(input('Веедите число: '))
i = 0
while 2 ** i <= n:
    print(f'{2 ** i}',end=' ')
    i += 1