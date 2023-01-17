# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.


def result1(my_list, j, k):
    return [my_list[j]*my_list[k]]

num = int(input('Введите число N: '))
print(list(range(-num,num+1)))
j =int(input('Введите номер позиции 1: '))
k=int(input('Введите номер позиции 2: '))
print(result1(list(range(-num,num+1)),j,k))

