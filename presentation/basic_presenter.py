from inputoutput.window_with_basic_relations import WindowWithBasicRelations
from presentation.presenter import Presenter


class BasicPresenter(Presenter):
# TODO how do we make BasicPresenter dynamically having initializators of relations
    def initialize_and_save_husband_of_relation(self, relation):
        self.initialize_relation(3, 1, "husband of relation (Чоловік)", relation, "Relation S")

    def initialize_and_save_father_in_law_of_relation(self, relation):
        self.initialize_relation(3, 2, "father-in-law relation (Тесть)", relation, "Relation R")

    def initialize_relation(self, row, column, long_title, relations, short_title):
        def build_and_show_relation():
            self.create_new_window(long_title)
            self.fill_cell_values(self, relations, short_title)

        assert isinstance(self.view, WindowWithBasicRelations)
        self.view.make_button(row, column, build_and_show_relation, short_title)