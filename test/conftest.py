import pytest

from binary_relation_generator import Person


@pytest.fixture
def righhanders():
    return {Person("male"), Person("female"), Person("male"), Person("male")}


@pytest.fixture
def male():
    return Person("male")

@pytest.fixture
def male1():
    return Person("male")

@pytest.fixture
def male2():
    return Person("male")

@pytest.fixture
def male3():
    return Person("male")


@pytest.fixture
def female():
    return Person("female")


@pytest.fixture
def female1():
    return Person("female")

@pytest.fixture
def female2():
    return Person("female")


@pytest.fixture
def female3():
    return Person("female")


@pytest.fixture
def dummy():
    class DummyPerson(object):
        pass
    return DummyPerson()


@pytest.fixture
def right_handed(male):
    return male

@pytest.fixture
def left_handed():
    return Person("male")
