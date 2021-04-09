from presentation.presenter import Presenter


class ComplexPresenter(Presenter):
    def present_U_diff_R_relation(self, relations):
        self.initialize_relation(3, 2, "father-in-law relation (Тесть)", relations, "Relation R")