import copy

from core.entity import Person


def convert_to_matrix(relations, table_name="Relation"):
    matrix = []
    domain = []
    codomain = []

    first_row = [table_name]
    for relation in relations:
        index_person_advanced(relation[1], codomain)
        first_row.append(relation[1].name)
    matrix.append(first_row)

    i = 1
    for relation in relations:

        domain_id = index_person_advanced(relation[0], domain)
        index_person_advanced(relation[1], codomain)
        try:
            matrix[domain_id] = [relation[0].name] + list("0" for _ in relations)
        except IndexError:
            matrix.append([relation[0].name] + list("0" for _ in relations))
        i += 1

    for relation in relations:
        try:
            domain_id = index_person_advanced(relation[0], domain)
            codomain_id = index_person_advanced(relation[1], codomain)
            matrix[domain_id][codomain_id] = "1"
        except IndexError:
            print("Index Error", relation[0].id + 1, relation[1].id + 1, relation)
    return matrix


def index_person_advanced(person: Person, out_cached_index):
    if person is None:
        raise ValueError()

    if person.name in out_cached_index:
        return out_cached_index.index(person.name) + 1
    else:
        out_cached_index.append(person.name)
        person.id = len(out_cached_index)
        return person.id


def find_names_of_people_with_no_relation(domain, relations):
    domain = copy.copy(domain)

    for relation in relations:
        if relation[0].name in domain:
            domain.remove(relation[0].name)
        if relation[1].name in domain:
            domain.remove(relation[1].name)
    return domain


def cast_to_names(set_of_persons):
    a = set()
    for person in set_of_persons:
        a.add(person.name)
    return a


class Presenter(object):
    def __init__(self, view):
        self.view = view

    def fill_cell_values(self, relations, group, relation_table_name):
        matrix = convert_to_matrix(relations, table_name=relation_table_name)
        codomain_no_connection = find_names_of_people_with_no_relation(group.B_names, relations)
        matrix[0] += codomain_no_connection

        domain_no_connection = find_names_of_people_with_no_relation(group.A_names, relations)
        for i in range(len(domain_no_connection)):
            name = domain_no_connection[i]
            matrix.append([name] + list("0" for _ in range(1, len(matrix[len(matrix) - 1]))))

        # normalization
        for i in range(1, len(matrix)):
            matrix[i] += list("0" for _ in range(len(matrix[0]) - len(matrix[i])))

        self.view.show_values_in_grid(matrix)

    def create_new_window(self, title):
        self.view.create_new_window(title)

    def initialize_relation(self, row, column, long_title, binary_relation, short_title, two_groups):
        def build_and_show_relation():
            self.create_new_window(long_title)
            self.fill_cell_values(binary_relation, two_groups, short_title)

        self.view.make_button(row, column, build_and_show_relation, short_title)