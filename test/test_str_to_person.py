from core.entity import Person
from core.entity_two_groups import cast_to_persons


def test_str_to_person():
    persons = cast_to_persons(["Anna", "Maxim", "Stas"])
    assert len(persons) == 3
    assert isinstance(persons.pop(), Person)