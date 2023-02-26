# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

# n, m, k = list(map(int, input('Введите необходимые параметры через пробел: ').split()))
# if k < n * m and k % n == 0 or k % m == 0:
#     print('Yes')
# else:
#     print('No')

# Решение с семинара

n = int(input('Задайте длинну шоколадки в дольках: '))
m = int(input('Задайте ширину шоколадки в дольках: '))
k = int(input('Задайте количество долек для отлома: '))

if (k % m == 0 or k % n == 0) and 0 < k < n * m:
    print('Yes')
else:
    print('No')