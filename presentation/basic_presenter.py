from inputoutput.window_with_basic_relations import WindowWithBasicRelations
from presentation.presenter import Presenter


class BasicPresenter(Presenter):
# TODO how do we make BasicPresenter dynamically having initializators of relations
    def initialize_and_save_husband_of_relation(self, relation):
        self.initialize_relation(3, 1, "husband of relation (Чоловік)", relation, "Relation S")

    def initialize_and_save_father_in_law_of_relation(self, relation):
        self.initialize_relation(3, 2, "father-in-law relation (Тесть)", relation, "Relation R")

