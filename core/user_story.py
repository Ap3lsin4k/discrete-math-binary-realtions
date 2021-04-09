from core import binary_relation_generator


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