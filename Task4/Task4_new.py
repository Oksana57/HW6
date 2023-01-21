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

def odd_find(in_num):
    if in_num%2 ==0:
        return True
    else:
        return False    

def not_odd_find(in_num):
    if in_num%2 !=0:
        return True
    else:
        return False   

def mixt(alist):
    new_list = alist[::-1]
    return new_list
    

a = int(input('ввеите цело число a: '))
b = int(input('ввеите цело число b: '))
n = int(input('ввеите цело число n: '))

rand_list1 = rand_list(a,b,n)
print(rand_list1)

list1=list(filter(odd_find, rand_list1))   
print(list1)
list2=list(filter(not_odd_find, rand_list1))   
print(list2)
list11=mixt(list1)
list21=mixt(list2)
print(list11)
print(list21)
list_mix=[*list11, *list21]
print(list_mix)

