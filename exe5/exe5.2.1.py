#Задание 5.2.1 (Конфеты человек с человеком)
from random import randint

def take(total, name):
    step = int(input(f'выбери количество конфет {name} = '))
    if total > max and step > max:
        step = max 
        print(f'удалось взять только {step} конфет')
    if total < step and step < max:
        step = total 
        print(f'удалось взять только {step} конфет')
    total = total - step
    if total > 0:
        print(f'осталось {total} конфет')
    else:
        print(f'УРА! конфеты закончились, победил {name}!')
    return total

print("На столе лежит 2021 конфета, за раз можно взять максимум 28, кто возьмет последние конфеты - получает все!")
p1 = input("Имя первого игрока:")
p2 = input("Имя второго игрока:")

if randint(1,2) == 2 : # бросаем жребий кто первый ходит
    t = p1
    p1 = p2 
    p2 = t

total = 2021
max = 28
p = 1

while total > 0:
    if p == 1 and total > 0: 
        total = take(total,p1)
        p = 2
    if p == 2 and total > 0:
        total = take(total,p2)
        p = 1



