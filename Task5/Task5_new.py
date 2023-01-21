# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def create_list (len1,num):
    new_list = []
    for i in range(len1):
        new_list.append(random.randint(1,num))
    return new_list    

def sum_odd(n_list):
    sum1=0
    for i in enumerate(n_list):
        if i[0]%2!=0:
            sum1=sum1 + n_list[i[0]]
    return sum1        


cl = create_list(int(input('введите длинну массива')),int(input('введите число')))  
print(cl)
sum_1 = sum_odd(cl)
print(sum_1)