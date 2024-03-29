# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты 
# высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля 
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает 
# ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# from random import randint

# N = int(input('Введите количество кустов на грядке: '))
# lst = [randint(1, N) for _ in range(N)]
# print(*lst)
# lst_2 = []

# for i in range(len(lst)):
#     lst_2.append(lst[i-2] + lst[i-1] + lst[i])

# # # так было в эталонном решении, но мой вариант вроде тоже работает правильно
# # for i in range(len(lst)-1):
# #     lst_2.append(lst[i-1] + lst[i] + lst[i+1])
# # lst_2.append(lst[-2] + lst[-1] + lst[0])  # описываем частный случай, который не попадает в первый "append()"

# print(max(lst_2))

# чутка слизал с эталонного решения


# ------------------------------------------------------------------------------------------------
# разбор на семинаре 

from random import randint

N = int(input('Введите количество кустов на грядке: '))
lst = [randint(1, N) for _ in range(N)]
print(*lst)
lst_2 = []

for _ in range(len(lst) - 2):
    a = lst[0] + lst[1] + lst[2] # считаются всегда первые три элемента
    lst.append(lst[0])           # потом в конец мы добавляем первый элемент      
    lst.remove(lst[0])           # и удалем его, тогда второй становится первым и считаются уже следующие три элемента
    lst_2.append(a)
print(max(lst_2))