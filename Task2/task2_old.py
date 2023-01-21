# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = float(input('Введите вещественное число: '))

str1=str(num)
print(str1)
str1=str1.replace('.','')

print(str1)
a=int(str1)
print(a)
sum = 0

while a >0:
    sum = sum + a%10
    a = a//10
print(round(sum, 2))




