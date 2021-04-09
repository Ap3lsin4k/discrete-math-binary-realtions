from core import binary_relation_generator as bin_relation
from presentation.controller import cast_to_persons


class TwoGroups:
    A_persons: set
    B_persons: set
    A_names: set
    B_names: set

    def __init__(self, left_handed, right_handed):
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
