from core import binary_relation_generator as bin_relation
from core.entity import Person

women_names = ["Вікторія", "Світлана", "Марія", "Анна", "Дарина", "Катерина", "Людмила", "Зоя", "Аліна", "Олена",
               "Юлія", "Лариса", "Анастасія", "Антоніна", "Оксана", "Галина", "Тетяна", "Василина", "Валентина", "Інна"]


def cast_to_persons(list_of_names) -> set:
    persons = set()
    for name in list_of_names:
        if name in women_names:
            persons.add(Person("female", name))
        else:
            persons.add(Person("male", name))
    return persons


class TwoGroups:
    A_persons: set
    B_persons: set
    A_names: set
    B_names: set

    def __init__(self, left_handed: set, right_handed: set):
        self.A_names = left_handed
        self.B_names = right_handed

    def cast_to_persons(self):
        self.A_persons = cast_to_persons(self.A_names)
        self.B_persons = cast_to_persons(self.B_names)
        return self


class TwoGroupsOfPersons:
    husband_of_relation: set
    father_in_law_of_relation: set

    def __init__(self, A_persons, B_persons, S, R):
        self.A_persons = A_persons
        self.B_persons = B_persons
        self.husband_of_relation = S
        self.father_in_law_of_relation = R

    def R_complement(self):
        U = bin_relation.generate_all_possible_relations(self.A_persons, self.B_persons)
        return U.difference(self.father_in_law_of_relation) #\R

    def cast_to_names(self):
        self.A_names = [x for x in self.A_persons]
        self.B_names = [x for x in self.B_persons]
        return self