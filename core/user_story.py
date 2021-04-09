class UserStory:
    def __init__(self, relation_generator, people):
        self.S_relations = set()
        self.R_relations = set()
        self.one_set = people.A_persons
        self.another_set = people.B_persons
        self.relation_generator = relation_generator

    def generate_relations(self):
        self.S_relations = self.relation_generator.generate_husband_relations_from_sets(self.one_set, self.another_set)
        self.R_relations = self.relation_generator.generate_random_father_in_law_relations_from_sets(self.one_set, self.another_set)

    def union(self):
        return self.S_relations | self.R_relations

    def intersection(self):
        return self.S_relations.intersection(self.R_relations)

    def difference(self):
        self.R_relations.difference(self.S_relations)

    def R_complement(self):
        U = self.relation_generator.generate_all_possible_relations(self.A_persons, self.B_persons)
        return U.difference(self.R_relations)  # \R