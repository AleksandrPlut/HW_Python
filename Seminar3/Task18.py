# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
mas = [randint(1, 100) for _ in range(int(input('Введите число цифр массива: ')))]
print(mas)
n = int(input('Введите искомое число в диапзоне от 1 до 100: '))
diff = 0
min_diff = 100
maxApprNum = 0
for i in mas:
    if i == n:
        print(f'Заданное Вами число {n} есть в массиве.')
    elif i > n:
        diff = i - n
        if diff < min_diff:
            min_diff = diff
            maxApprNum = i
    elif i < n:
        diff = (i - n) * -1
        if diff < min_diff:
            min_diff = diff
            maxApprNum = i
print(f'Максимально близкое к заданному числу {n}, соответствует число {maxApprNum}.')

# вроде и решил, но результат не нравится, если заданное число есть в массиве, 
# помимо сообющения о том, что искомое число есть в массиве, он все равно дополнительно выдает сообщение
# ближайшее число

# ну и опять же не уверен, что я правильно понял условия задачи
