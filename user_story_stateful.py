class UserStory:
    def __init__(self, relation_generator, one_set, another_set):
        self.S_relations = None
        self.R_relations = None
        self.another_set = another_set
        self.one_set = one_set
        self.relation_generator = relation_generator

    def generate_relations(self):
        self.S_relations = self.relation_generator.generate_husband_relations_from_sets(self.one_set, self.another_set)
        self.R_relations = self.relation_generator.generate_father_in_law_relations_from_sets(self.one_set, self.another_set)