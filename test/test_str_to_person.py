import controller
from entity import Person


def test_str_to_person():
    persons = controller.cast_to_persons(["Anna", "Maxim", "Stas"])
    assert len(persons) == 3
    assert isinstance(persons.pop(), Person)