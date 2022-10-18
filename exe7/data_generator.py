# pip install mimesis - библиотека для генерации данных
from random import choice
from mimesis import Person
from mimesis.builtins import RussiaSpecProvider
from mimesis.enums import Gender

def get_person(): # генерация строчки в справочник
    person = Person('ru')
    ru_spec = RussiaSpecProvider()
    gender = choice([Gender.MALE,Gender.FEMALE]) 

    result = [person.first_name(gender=gender), ru_spec.patronymic(gender=gender), person.last_name(gender=gender), 
                person.telephone(mask='+7-9##-###-####')]
    if choice([1,2]) == 2: result.append(person.telephone(mask='+7-9##-###-####'))
    return result


