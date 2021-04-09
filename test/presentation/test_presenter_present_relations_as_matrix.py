# ['Катерина', 'Адам', 'Щек', 'Ігор', 'Віктор', 'Гліб', 'Данило', 'Євген', 'Дмитро', 'Вадим', 'Олег', 'Михайло', 'Людмила']
# ['Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя', 'Аліна']
# self.us.generate_relations()
# self.us.R_relations
import pickle

from core import binary_relation_generator
from core.complex_user_story import ComplexUserStory
from core.entity_two_groups import TwoGroups
from presentation.complex_presenter import ComplexPresenter
from presentation.presenter import Presenter
from core.user_story import UserStory


class UISpy():
    def show_values_in_grid(self, matrix):
        self.matrix = matrix


def test_fill_cell_values():
    left_handed_names = ['Катерина', 'Адам', 'Щек', 'Ігор', 'Віктор', 'Гліб', 'Данило', 'Євген', 'Дмитро', 'Вадим',
                         'Олег', 'Михайло', 'Людмила']
    set_B_names = ['Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя',
                   'Аліна']
    ui = UISpy()

    presenter = Presenter(TwoGroups(['Катерина', 'Адам', 'Щек', 'Ігор', 'Віктор', 'Гліб', 'Данило', 'Євген', 'Дмитро', 'Вадим',
                   'Олег', 'Михайло', 'Людмила'],
                  ['Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя',
                   'Аліна']),
        ui)
    us = UserStory(binary_relation_generator, TwoGroups(left_handed_names,
                                                        set_B_names).cast_to_persons(), presenter=None)
    us.generate_relations()
    presenter.fill_cell_values(us.R_relations, "Relation")

    assert set(ui.matrix[0][1:]).difference(
        {'Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя',
         'Аліна'}) == set()
    assert len(set(ui.matrix[0][1:]).difference(
        {'Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя',
         'Аліна'})) == 0
    assert set(i[0] for i in ui.matrix if i[0] != "Relation").difference(
        {'Катерина', 'Адам', 'Щек', 'Ігор', 'Віктор', 'Гліб', 'Данило', 'Євген', 'Дмитро', 'Вадим',
         'Олег', 'Михайло', 'Людмила'}) == set()

    assert ui.matrix[1][-1] == "0"
    assert len(ui.matrix[0]) == len(ui.matrix[1])



def test_fill_cell_values_small_data():
    left_handed_names = ['Катерина', 'Адам', 'Щек']
    set_B_names = ['Олександр', 'Віталій', 'Богдан', "Аліна"]
    ui = UISpy()

    presenter = Presenter(TwoGroups(left_handed_names,
                                    set_B_names), ui)
    us = UserStory(binary_relation_generator, TwoGroups(left_handed_names,
                                                        set_B_names).cast_to_persons(), presenter=None)
    us.generate_relations()
    presenter.fill_cell_values(us.R_relations, "Relation R")
    assert "Аліна" in ui.matrix[0]
    assert len(set(ui.matrix[0]).difference(
        {"Relation R", 'Олександр', 'Віталій', 'Богдан', "Аліна"})) == 0
    assert len(ui.matrix[0]) == 5
    assert len(ui.matrix[1]) == 5
    assert len(ui.matrix[2]) == 5
    assert len(ui.matrix[3]) == 5
    assert len(ui.matrix) == 4



