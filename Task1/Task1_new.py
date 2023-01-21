# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

num = int(input('Введите число N: '))
alist = [i for i in range (-num,num+1)]

print(alist)
j =int(input('Введите номер позиции 1: '))
k=int(input('Введите номер позиции 2: '))
f=lambda j, k: alist[j]*alist[k]

print(f( j, k))

