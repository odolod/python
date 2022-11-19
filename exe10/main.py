from data_generator import generate
from UI import show_menu, add_employee, delete_employee, export_cvs, export_json, find_employee, find_employee_positon, find_employee_salary, update_employee

n = int(input("Сколько сотрудников сгенерировать?(0 - генерация не требуется) "))
if n != 0: generate(n)

choice = 0
while choice != 9 :
    choice = show_menu()
    match choice:
        case 1: find_employee() 
        case 2: find_employee_positon() 
        case 3: find_employee_salary() 
        case 4: add_employee()
        case 5: delete_employee() 
        case 6: update_employee()
        case 7: export_json()
        case 8: export_cvs() 
        case _: 
            if choice !=9: print(f"Команда {choice} не распознана")