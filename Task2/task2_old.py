# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = float(input('Введите вещественное число: '))
num = num*(10**5)
sum = 0

f=lambda num: num%10

while num >0:
    sum = sum + num%10
    num = num//10
print(round(sum, 2))

