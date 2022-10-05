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
print("Простые множители N:", res)
# Задание 4.3

# Задание 4.4

# Задание 4.5