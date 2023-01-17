# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.


def result1(my_list, j, k):
    for i in my_list:
        result = my_list[j]*my_list[k]
    return result

num = int(input('Введите число N: '))
my_list = list(range(-num,num+1))
print(my_list)
j=int(input('Введите номер позиции 1: '))
k=int(input('Введите номер позиции 2: '))
result_j_k = result1(my_list,j,k)
print(result_j_k)

