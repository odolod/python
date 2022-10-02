# Задание 2.1
a = float(input('Введите вещественное число:'))
s = 0
for x in str(a): 
    if x != '.' and x != ',': s += int(x)
print('Сумма цифр:', s)    
# Задание 2.2
def fact (n, mul = 1):
    for i in range(1, n + 1):
        mul *= i
    return mul

n = int(input('Введите число N:'))
print([fact(x) for x in range(1,n+1)])
# Задание 2.3
n = int(input('Введите число N:')) 

seq = [(1 + 1 / x)**x for x in range (1, n + 1)]
ss = [round(sum(seq[0:y])) for y in range (1, n + 1)]
l = dict(zip(range(1,n+1),ss))        
print(l)
# Задание 2.4.1
n = int(input('Введите число N:')) 
from random import randint
nums = [randint (-n,n) for y in range(n)]
print("Массив:",nums)
mul = 1
data = open('file.txt', 'r')
for line in data:
    mul *= nums[int(line)-1]
data.close()
print("Произведение на позициях из файла:", mul)
# Задание 2.4.2
from random import randint
nums = [randint (0,100) for y in range(10)]
print("Начальный список:",nums)
for x in range(150): # сколько раз менять
    i = randint (0,9)
    j = randint (0,9)
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t
print("Перемешанный список:",nums)
