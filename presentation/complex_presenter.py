from presentation.presenter import Presenter


class ComplexPresenter(Presenter):

    def present_R_unioun_S_relation(self, relations):
        self.initialize_relation(1, 0, "Одружені чоловіки АБО тесті", relations, "R ∪ S")

    def present_R_intersection_S_relation(self, relations):
        self.initialize_relation(2, 0, "Одружені чоловіки і тесті", relations, "R ∩ S")

    def present_R_difference_S_relation(self, relations):
        self.initialize_relation(3, 0, "Одружені чолівіки \ тесті", relations, "R \ S")

    def present_U_diff_R_relation(self, relations):
        self.initialize_relation(4, 0, "U difference Тесть", relations, "U \ R")

    def present_inverse_of_S(self, relations):
        self.initialize_relation(5, 0, "Обернене відношення до одружених чоловіків", relations, "S ** (-1)")