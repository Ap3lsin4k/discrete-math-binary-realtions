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


class ComplexUserStory(UserStory):

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
        #self.presenter.create_new_window("U \ R")
        # presenter = Presenter(self.two_groups.cast_to_names(), )
        # presenter.fill_cell_values(self.two_groups.R_complement(), "U \ R")
        return self.two_groups.R_complement()
