from database import read_json, write_csv, write_json

def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате cvs")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))  

def find_employee(text='Введите строку для поиска:'):
    employees = read_json()
    find = input(text)
    for i in employees:
        for j in i.values():
            if find in str(j): print(i)

def find_employee_positon(text='Введите должность:'):
    employees = read_json()
    find = input(text)
    for i in employees:
        if find in str(i['position']): print(i)

def find_employee_salary():
    employees = read_json()
    l = float(input("Введите нижный уровень зарплаты:"))
    h = float(input("Введите верхний уровень зарплаты:"))
    for i in employees:
        if l < i['salary'] and h > i['salary']: print(i)

def add_employee():
    id = int(input("Введите id:"))
    last_name = input("Введите фамилию:")
    first_name = input("Введите имя:")
    position = input("Введите должность:")
    phone_number = input("Введите телефон:")
    salary = float(input("Введите зарплату:"))
    employees = read_json()
    employees.append({'id': id, 'last_name': last_name, 'first_name': first_name, 'position': position, 'phone_number': phone_number, 'salary': salary})
    write_json(employees)
    write_csv(employees)
    print("Сотрудник добавлен")

def delete_employee():
    id = int(input("Введите id сотрудника для удаления:"))
    employees = read_json()
    for i in employees:
        if id == i['id']: employees.remove(i)
    write_json(employees)
    write_csv(employees)
    print("Сотрудник удален")

def update_employee():
    id = int(input("Введите id сотрудника для изменения:"))
    last_name = input("Введите фамилию:")
    first_name = input("Введите имя:")
    position = input("Введите должность:")
    phone_number = input("Введите телефон:")
    salary = float(input("Введите зарплату:"))
    employees = read_json()
    for i in employees:
        if id == i['id']: i.update({'id': id, 'last_name': last_name, 'first_name': first_name, 'position': position, 'phone_number': phone_number, 'salary': salary})
    write_json(employees)
    write_csv(employees)
    print("Сотрудник изменен")

def export_json():
    employees = read_json()
    write_json(employees)
    print("Данные экспортированы в database.json")

def export_cvs():
    employees = read_json()
    write_csv(employees)
    print("Данные экспортированы в database.cvs")

