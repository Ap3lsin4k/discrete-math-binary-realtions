#['Катерина', 'Адам', 'Щек', 'Ігор', 'Віктор', 'Гліб', 'Данило', 'Євген', 'Дмитро', 'Вадим', 'Олег', 'Михайло', 'Людмила']
#['Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя', 'Аліна']
#self.us.generate_relations()
#self.us.R_relations
import binary_relation_generator
from controller import cast_to_persons
from presenter import Presenter
from user_story_stateful import UserStory


class UISpy():
    def show_values_in_grid(self, matrix):
        self.matrix = matrix


def test_fill_cell_values():
    left_handed_names = ['Катерина', 'Адам', 'Щек', 'Ігор', 'Віктор', 'Гліб', 'Данило', 'Євген', 'Дмитро', 'Вадим',
                          'Олег', 'Михайло', 'Людмила']
    right_handed_names = ['Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя',
                          'Аліна']
    presenter = Presenter(left_handed_names=['Катерина', 'Адам', 'Щек', 'Ігор', 'Віктор', 'Гліб', 'Данило', 'Євген', 'Дмитро', 'Вадим', 'Олег', 'Михайло', 'Людмила'],
                          right_handed_names=['Олександр', 'Віталій', 'Богдан', 'Сергій', 'Микола', 'Володимир', 'Юрій', 'Семен', 'Зоя', 'Аліна'],
                          )
    us = UserStory(binary_relation_generator, cast_to_persons(right_handed_names),
                            cast_to_persons(left_handed_names))
    us.generate_relations()
    ui = UISpy()
    presenter.fill_cell_values(ui, us.R_relations, None)
    assert ui.matrix is not None

