from core.entity_two_groups import TwoGroupsAndTwoRelations, TwoGroups
from core.user_story import UserStory
from presentation.complex_presenter import ComplexPresenter
from presentation.presenter import Presenter


class ComplexUserStory(UserStory):

    def union(self):
        return self.two_groups.father_in_law_of_relation | self.two_groups.husband_of_relation

    def intersection(self):
        return self.two_groups.husband_of_relation.intersection(self.two_groups.father_in_law_of_relation)

    def difference(self):
        return self.two_groups.father_in_law_of_relation.difference(self.two_groups.husband_of_relation)

    def R_complement(self):
        U = self.relation_generator.generate_all_possible_relations(self.A_persons, self.B_persons)
        return U.difference(self.two_groups.father_in_law_of_relation)

    def U_diff_R(self):
        assert isinstance(self.presenter, Presenter)
        #self.presenter.create_new_window("U \ R")
        # presenter = Presenter(self.two_groups.cast_to_names(), )
        # presenter.fill_cell_values(self.two_groups.R_complement(), "U \ R")
        return self.two_groups.R_complement()

    def intialize_and_save_U_diff_R_relation(self):
        assert isinstance(self.presenter, ComplexPresenter)
        self.presenter.present_U_diff_R_relation(self.two_groups.R_complement())

    def execute(self):
        self.presenter.present_R_unioun_S_relation(self.union(), self.two_groups)
        self.presenter.present_R_intersection_S_relation(self.intersection(), self.two_groups)
        self.presenter.present_R_difference_S_relation(self.difference(), self.two_groups)
        self.presenter.present_U_diff_R_relation(self.two_groups.R_complement(), self.two_groups)
        inverse_of_two_groups = TwoGroupsAndTwoRelations(self.two_groups.B_persons, self.two_groups.A_persons, S=None, R=None)
        self.presenter.present_inverse_of_S(self.inverse_of_S(), inverse_of_two_groups)

    def inverse_of_S(self):
        inverse_relation = set()
        for relation in self.two_groups.husband_of_relation:
            inverse_relation.add((relation[1], relation[0]))
        return inverse_relation