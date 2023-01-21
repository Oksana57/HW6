# 5 Реализуйте алгоритм перемешивания списка.


import random

def rand_list(a,b,n):
    alist = []
    for i in range(n):
        if a<b:
             k = random.randint(a,b)
        else:
             k= random.randint(b,a)
        alist.append(k)
    return alist

def mixt(alist):
    new_list = []
    k = len(alist)
    for i in alist:
        new_list.append(alist[k-1])
        k-=1
    return new_list


a = int(input('ввеите цело число a: '))
b = int(input('ввеите цело число b: '))
n = int(input('ввеите цело число n: '))

rand_list1 = rand_list(a,b,n)

print(rand_list1)
mixt1 = mixt(rand_list1)
print(mixt1)

