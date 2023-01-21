# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = float(input('Введите вещественное число: '))

str1=int(str(num).replace('.',''))
print(str1)
sum=0
f=lambda str1: str1%10
while str1>0:
    sum+=f(str1)
    str1=str1//10
print(sum)





