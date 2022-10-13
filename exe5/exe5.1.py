#Задание 5.1
str = input("Введите текст:").replace("абв","")
print("Текст без 'абв':",str)

#правильное решение
PATTERN = 'абв'
my_text = 'арбуз абвгд был абвгд красным'

print(' '.join([word for word in my_text.split() if not PATTERN in word]))