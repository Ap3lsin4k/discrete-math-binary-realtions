class UserStory:
    def __init__(self, relation_generator, people):
        self.S_relations = None
        self.R_relations = None
        self.one_set = people.A
        self.another_set = people.B
        self.relation_generator = relation_generator

    def generate_relations(self):
        self.S_relations = self.relation_generator.generate_husband_relations_from_sets(self.one_set, self.another_set)
        self.R_relations = self.relation_generator.generate_father_in_law_relations_from_sets(self.one_set, self.another_set)