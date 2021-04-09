from presentation.presenter import Presenter


class UserStory:
    def __init__(self, relation_generator, people, presenter):
        self.S_relations = set()
        self.R_relations = set()
        self.one_set = people.A_persons
        self.another_set = people.B_persons
        self.relation_generator = relation_generator
        self.two_groups = people
        self.presenter = presenter

    def generate_relations(self):
        self.S_relations = self.relation_generator.generate_husband_relations_from_sets(self.one_set, self.another_set)
        self.R_relations = self.relation_generator.generate_random_father_in_law_relations_from_sets(self.one_set,
                                                                                                     self.another_set)

    def union(self):
        return self.S_relations | self.R_relations

    def intersection(self):
        return self.S_relations.intersection(self.R_relations)

    def difference(self):
        self.R_relations.difference(self.S_relations)

    def R_complement(self):
        U = self.relation_generator.generate_all_possible_relations(self.A_persons, self.B_persons)
        return U.difference(self.R_relations)  # \R

    def U_diff_R(self):
        assert isinstance(self.presenter, Presenter)
        self.presenter.create_new_window("U \ R")
        # presenter = Presenter(self.two_groups.cast_to_names(), )
        # presenter.fill_cell_values(self.two_groups.R_complement(), "U \ R")
        return self.two_groups.R_complement()

    def build_and_show_relation(self, title, relations, relation_table_name):
        self.presenter.fill_cell_values(self, relations, relation_table_name)

        self.presenter.fill_cell_values(self, relations, relation_table_name)

    def initialize_relation(self, row, column, long_title, relation, short_title):
        def build_and_show_relation():
            self.__build_and_show_relation(long_title, relation, short_title)

        self.presenter.make_button(row, column, build_and_show_relation, short_title)

    def __build_and_show_relation(self, title, relations, relation_table_name):
        self.presenter.create_new_window(title)
        self.presenter.fill_cell_values(self, relations, relation_table_name)

    def initialize_and_save_father_in_law_of_relation(self):
        def build_and_show_relation():
            self.presenter.create_new_window("father-in-law relation (Тесть)")
            self.presenter.fill_cell_values(self, self.us.R_relations, "Relation R")

        self.presenter.make_button(self.root_relation_controller, row, column, build_and_show_relation, short_title)

        self.initialize_relation(3, 2, "father-in-law relation (Тесть)", self.us.R_relations, "Relation R")
