# Задание 3.1
from random import randint
nums = [randint (0,10) for y in range(randint (4,10))]
print("Cписок:",nums)
s = 0
for i in range(len(nums)):
    if i % 2 != 0: s += nums[i]
print("Сумма элементов на нечетных позициях:",s)    
# Задание 3.2
from random import randint
nums = [randint (0,10) for y in range(randint (4,10))]
print("Cписок:",nums)
mul = [nums[i]*nums[len(nums)-1-i] for i in range((len(nums)+1)//2)]
print("Произведения пар:",mul)  
# Задание 3.3
from random import randint, random
nums = [round(random()+randint(0,10),2) for y in range(randint (4,10))]
print("Cписок:",nums)
ost = [round(nums[i]%1,2) for i in range(len(nums))]
print("разница между максимальным и минимальным значением дробной части элементов:",max(ost)-min(ost))
# Задание 3.4
n = int(input('Введите число N:')) 
res = ''
while n > 0:
    res = str(n % 2) + res
    n = n // 2
print("N в двоичном виде:", res)
# Задание 3.5
n = int(input('Введите число N>2:'))
fib = list(range(2)) 
for i in range(2,n+1): fib += [fib[i-1]+fib[i-2]] 
fibn = [(-1)**(i+1)*fib[i] for i in range(1,n+1)] 
fibn.reverse()
print(fibn + fib)
