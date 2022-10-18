n = int(input('Введите количество записей в справочнике: '))

txt_file_name = 'phonebook.txt'
cvs_file_name = 'phonebook.cvs'

from data_generator import get_person
from export_file import save_txt_file
from export_file import save_cvs_file
from import_file import load_txt_file
from import_file import load_cvs_file

data = [get_person() for x in range(n)]
save_txt_file(txt_file_name, data)
save_cvs_file(cvs_file_name, data)
print(f'Данные сохранены в файл {txt_file_name} и в файл {cvs_file_name}')

print(f"Данные из {txt_file_name}:", load_txt_file(txt_file_name))
print('-'*42)
print(f"Данные из {cvs_file_name}:", load_cvs_file(cvs_file_name))
print('-'*42)