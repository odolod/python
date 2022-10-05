# Задание 4.1
from math import radians, sin
d = float(input('Введите число d(0,1 ≤ d ≤ 0,00000000001:')) 
pi = radians((1/d*50)*(sin(180/(1/d*50)))) # можно вычислять разными методами, ряды и т.д.
print(pi, "Вычисленное значение")
print("3,1415926535897932", "Эталонное значение")
# Задание 4.2
def findP(x):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307]
    for i in range(len(primes)): 
      #  print(primes[i])
        if x % primes[i] == 0 : return primes[i]
    else: return x

def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

n = int(input('Введите число N:'))
res = []
while not is_prime(n):
    p = findP(n)
    res.append(p)
    n //= p  
res.append(n)    
print("Простые множители N:", res) # результат может быть не верным при N > 800000
# Задание 4.3
from random import randint
nums = [randint (0,15) for y in range(randint (10,20))]
print("Cписок:",nums)
res = []
for i in range(len(nums)):
    if nums.count(nums[i]) == 1 : res.append(nums[i])
print("Список неповторяюшихся элементов:", res)
# Задание 4.4 
k = int(input('Введите степень многочлена k:'))
from random import randint
nums = [randint (0,100) for y in range(k+1)]
with open('polynomial.txt', 'w') as data:
    for i in (range(k-1)):
        if nums[i] != 0 : data.write(f'{nums[i]}*x^{k-i} + ')
    if nums[len(nums)-2] != 0 : data.write(f'{nums[len(nums)-2]}*x + ')
    data.write(f'{nums[len(nums)-1]} = 0')
print("Результат в файле polynomial.txt")
# Задание 4.5
with open('polynomial1.txt','r') as data:
    pol1 = data.readline()
with open('polynomial2.txt','r') as data:
    pol2 = data.readline()

def makeDict(pol):
    pol = pol.replace(" = 0","")
    pol = pol.replace("*x^","|")
    pol = pol.split(" + ")
    for i in range(len(pol)):
        if str(pol[i]).isdigit() : pol[i] = [pol[i], 0]
        elif pol[i].find('*x') > 0 : pol[i] = [pol[i].replace('*x', ''), 1]
        else: pol[i] = pol[i].split('|')
    for i in range(len(pol)): 
        pol[i] = [int(pol[i][1]),int(pol[i][0])] 
    return dict(pol)

def sumDict(d1, d2):
    for key, value in d1.items():
        d1[key] = value + d2.get(key, 0)
    return d1

pol1 = makeDict(pol1)
pol2 = makeDict(pol2)
if len(pol1) > len(pol2) : res = sumDict(pol1,pol2)
else: res = sumDict(pol2,pol1)

with open('polynomialsum.txt', 'w') as data:
    for key, value in res.items():
        if key > 1 : data.write(f'{value}*x^{key} + ')
        elif key == 1 : data.write(f'{value}*x + ')
        else: data.write(f'{value} = 0')

print("Результат в файле polynomialsum.txt") # Предпологается что коэффициенты многочленов положительные
