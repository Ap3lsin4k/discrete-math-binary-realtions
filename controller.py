from entity import Person


women_names = ["Вікторія", "Світлана", "Марія", "Анна", "Дарина", "Катерина", "Людмила", "Зоя", "Аліна", "Олена",
               "Юлія", "Лариса", "Анастасія", "Антоніна", "Оксана", "Галина", "Тетяна", "Василина", "Валентина", "Інна"]


def cast_to_persons(list_of_names):
    persons = set()
    for name in list_of_names:
        if name in women_names:
            persons.add(Person("female", name))
        else:
            persons.add(Person("male", name))
    return persons