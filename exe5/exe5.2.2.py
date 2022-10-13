#Задание 5.2.2 (Конфеты человек с тупым ботом)
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

def take_bot(total, name):
    step = randint(1,max)
    print(f'выбери количество конфет {name} = {step}')
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
p1 = input("Имя игрока:")
p2 = "тупой бот"
bot = 2

if randint(1,2) == 2 : # бросаем жребий кто первый ходит
    t = p1
    p1 = p2 
    p2 = t
    bot = 1

total = 2021
max = 28
p = 1

while total > 0:
    if p == 1 and total > 0: 
        if bot == 1: total = take_bot(total,p1)
        else: total = take(total,p1)
        p = 2
    if p == 2 and total > 0:
        if bot == 2: total = take_bot(total,p2)
        else: total = take(total,p2)
        p = 1



