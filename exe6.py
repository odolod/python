# Задание 2.1 - изначальное
a = float(input('Введите вещественное число:'))
s = 0
for x in str(a): 
    if x != '.' and x != ',': s += int(x)
print('Сумма цифр:', s) 
# Задание 2.1 - переписанное
a = float(input('Введите вещественное число:'))
print('Сумма цифр:', sum(map(lambda x: int(x), filter(lambda x: x.isdigit(), str(a)))))


# Задание 3.1 - изначальное
from random import randint
nums = [randint (0,10) for y in range(randint (4,10))]
print("Cписок:",nums)
s = 0
for i in range(len(nums)):
    if i % 2 != 0: s += nums[i]
print("Сумма элементов на нечетных позициях:",s) 
# Задание 3.1 - переписанное
from random import randint
nums = [randint (0,10) for y in range(randint (4,10)) if y % 2 != 0]
print("Сумма элементов на нечетных позициях:", sum(nums))

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
# Задание 4.4 - переписанное
k = int(input('Введите степень многочлена k:'))
from random import randint
poly = dict(zip(list(range(k, -1, -1)), map(lambda x:randint (0,100), list(range(k+1)))))

def get_member(k, b):
    if k == 0: return str(b) 
    elif k == 1: return str(f'{b}*x + ')
    else: return str(f'{b}*x^{k} + ')    

with open('polynomial.txt', 'w') as data:
    list(map(lambda x: data.write(get_member(x,poly[x])), poly))
    data.write(' = 0')
print("Результат в файле polynomial.txt")

