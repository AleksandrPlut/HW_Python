# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = int(input('Введите трехзначное, целое число: '))
sum = 0
while a > 0:
    sum += a % 10
    a = a // 10
print(sum)


# Решение с семинара

# number = int(input('Введите трехзначное, целое число: '))
# if 99 < number < 1000:
#     arrayNumber = map(int, str(number))
#     # sumDigits = arrayNumber[0] + arrayNumber[1] + arrayNumber[2]
#     sumDigits = sum(arrayNumber) # функцией "sum" заменили то что написано выше
#     print(sumDigits)
# else:
#     print('введен некоректный номер')

# Решение с семинара (сложное)

# my_num = input('Введите число: ')

# def digit_sum(num2chek): # тут вводим любые цифры, буквы, тип "str"
#     sum_num = 0
#     for i in range(len(num2chek)):
#         if num2chek[i].isdigit(): # функция ".isdigit" пробегает по всей строке, находит в ней цифры и записывает их переменную
#             temp = int(num2chek[i]) 
#             sum_num = sum_num + temp
#     return sum_num
# print('Сумма цыфр в числе', my_num, 'равна', DC(my_num)) # а тут какаято непонятка, чувак слишком умно все делает, так и не смог добить

