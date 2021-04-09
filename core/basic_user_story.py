from core.user_story import UserStory
from presentation.presenter import Presenter
from presentation.basic_presenter import BasicPresenter


class BasicUserStory(UserStory):

    def execute(self):
        self.presenter.initialize_and_save_husband_of_relation(self.S_relations, self.two_groups)
        self.presenter.initialize_and_save_father_in_law_of_relation(self.R_relations, self.two_groups)
