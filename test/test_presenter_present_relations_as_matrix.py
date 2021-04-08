# ['Катерина', 'Адам', 'Щек', 'Ігор', 'Віктор', 'Гліб', 'Данило', 'Євген', 'Дмитро', 'Вадим', 'Олег', 'Михайло', 'Людмила']
# ['Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя', 'Аліна']
# self.us.generate_relations()
# self.us.R_relations
import binary_relation_generator
from controller import cast_to_persons
from entity_two_groups import TwoGroups
from presenter import Presenter
from user_story_stateful import UserStory


class UISpy():
    def show_values_in_grid(self, matrix):
        self.matrix = matrix


def test_fill_cell_values():
    left_handed_names = ['Катерина', 'Адам', 'Щек', 'Ігор', 'Віктор', 'Гліб', 'Данило', 'Євген', 'Дмитро', 'Вадим',
                         'Олег', 'Михайло', 'Людмила']
    set_B_names = ['Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя',
                   'Аліна']
    presenter = Presenter(
        TwoGroups(['Катерина', 'Адам', 'Щек', 'Ігор', 'Віктор', 'Гліб', 'Данило', 'Євген', 'Дмитро', 'Вадим',
               'Олег', 'Михайло', 'Людмила'],
        ['Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя',
               'Аліна'])
    )
    us = UserStory(binary_relation_generator, TwoGroups(left_handed_names,
                   set_B_names).cast_to_persons())
    us.generate_relations()
    ui = UISpy()
    presenter.fill_cell_values(ui, us.R_relations, None)

    assert set(ui.matrix[0][1:]).difference(
        {'Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя',
         'Аліна'}) == set()
    assert len(set(ui.matrix[0][1:]).difference(
        {'Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя',
         'Аліна'})) == 0
    assert set(i[0] for i in ui.matrix if i[0] is not None).difference(
        {'Катерина', 'Адам', 'Щек', 'Ігор', 'Віктор', 'Гліб', 'Данило', 'Євген', 'Дмитро', 'Вадим',
         'Олег', 'Михайло', 'Людмила'}) == set()

    assert ui.matrix[1][-1] == "0"
    assert len(ui.matrix[0]) == len(ui.matrix[1])



def test_fill_cell_values_small_data():
    left_handed_names = ['Катерина', 'Адам', 'Щек']
    set_B_names = ['Олександр', 'Віталій', 'Богдан', "Аліна"]
    presenter = Presenter(
        TwoGroups(left_handed_names,
        set_B_names)
    )
    us = UserStory(binary_relation_generator, TwoGroups(left_handed_names,
                   set_B_names).cast_to_persons())
    us.generate_relations()
    ui = UISpy()
    presenter.fill_cell_values(ui, us.R_relations, "Relation R")
    assert "Аліна" in ui.matrix[0]
    assert len(set(ui.matrix[0]).difference(
        {"Relation R", 'Олександр', 'Віталій', 'Богдан', "Аліна"})) == 0
    assert len(ui.matrix[0]) == 5
    assert len(ui.matrix[1]) == 5
    assert len(ui.matrix[2]) == 5
    assert len(ui.matrix[3]) == 5
    assert len(ui.matrix) == 4
