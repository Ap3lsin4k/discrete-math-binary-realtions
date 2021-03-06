import pytest

from core import binary_relation_generator
from core.entity import Person
from core.entity_two_groups import TwoGroups
from core.user_story import UserStory
from presentation.controller import Controller
from presentation.presenter import convert_to_matrix, Presenter
from inputoutput.window_with_basic_relations import WindowWithBasicRelations


def test_ui_intergration_with_us(male, male1, male2, male3, female, female1, female2, female3):
    us = UserStory(binary_relation_generator,
              TwoGroups(["Michael"], ["Mike"]).cast_to_persons(),
                   presenter=None)
    us.generate_relations()
    controller = Controller(us)

    assert controller.us.R_relations
    assert len(controller.us.R_relations) == 1
    assert len(controller.us.S_relations) == 0


def test_controller_intergration_with_us(male, male1, male2, male3, female, female1, female2, female3):
    us = UserStory(binary_relation_generator,
              TwoGroups(["Michael"], ["Mike"]).cast_to_persons(), presenter=None)
    us.generate_relations()

    assert us.R_relations
    assert len(us.R_relations) == 1
    assert len(us.S_relations) == 0



def test_convert_relation_to_matrix(male, female, male1, male2, female2):
    relations = ((male, female), (male2, male1), (female2, male))
    matrix = convert_to_matrix(relations)
    assert matrix[0][1] == female.name
    assert matrix[1][0] == male.name
    assert matrix[1][1] == "1"

    assert matrix[0][2] == male1.name
    assert matrix[2][0] == male2.name
    assert matrix[1] == [male.name, "1", "0", "0"]
    assert matrix[2] == [male2.name, "0", "1", "0"]
    assert matrix[3] == [female2.name, "0", "0", "1"]


@pytest.mark.skip("Impossible case")
def test_convert_relation_to_matrix(male, female, male1, male2, female2):
    relations = ((male, female), (male2, female))
    matrix = convert_to_matrix(relations)
    assert matrix[0][1] == female.name
    assert matrix[1][0] == male.name
    assert matrix[0][2] == female.name
    assert matrix[2][0] == male2.name
    assert matrix[1] == [male.name, "1", "0"]
    assert matrix[2] == [male2.name, "1", "0"]

def test_convert_relation_to_matrix3(male, female, male1, male2, female2):
    relations = ((male, female), (male2, male1), (male, female2))
    matrix = convert_to_matrix(relations)
    assert matrix[0] == ["Relation", female.name, male1.name, female2.name]

    Adam = Person("male", "????????")
    matrix = convert_to_matrix((
        (Adam, Person("male", "??????????????????")),
        (Adam, Person("male", "??????????????"))
    ))
    assert matrix == [['Relation', '??????????????????', '??????????????'], ['????????', '1', '1']]
def test_convert_relation_to_matrix4(male, female, male1, male2, female2):

    Adam = Person("male", "????????")
    matrix = convert_to_matrix((
        (Adam, Person("male", "??????????????????")),
        (Adam, Person("male", "??????????????")),
        (Person("male", "??????"), Person("male", "????????????")),
        (Person("male", "????????"), Person("male", "??????????")),
        (Person("male", "????????"), Person("male", "??????????"))
    ))
    assert matrix == [['Relation', '??????????????????', '??????????????', "????????????", "??????????", "??????????"],
                      ['????????', '1', '1', '0', '0', '0'],
                      ['??????', '0', '0', '1', '0', '0'],
                      ['????????', '0', '0', '0', '1', '1'],]


#    convert_to_matrix((male, male1))

