from presentation.presenter import Presenter


class ComplexPresenter(Presenter):

    def present_R_unioun_S_relation(self, relations, two_groups):
        self.initialize_relation(1, 0, "тесті АБО одружені чоловіки", relations, "R ∪ S", two_groups)

    def present_R_intersection_S_relation(self, relations, two_groups):
        self.initialize_relation(2, 0, "Тесті і одружені чоловіки", relations, "R ∩ S", two_groups)

    def present_R_difference_S_relation(self, relations, two_groups):
        self.initialize_relation(3, 0, "Тесті \ одружені чоловіки", relations, "R \ S", two_groups)

    def present_U_diff_R_relation(self, relations, two_groups):
        self.initialize_relation(4, 0, "U difference Тесть", relations, "U \ R", two_groups)

    def present_inverse_of_S(self, relations, two_groups):
        self.initialize_relation(5, 0, "Обернене відношення до одружених чоловіків", relations, "S ** (-1)", two_groups)