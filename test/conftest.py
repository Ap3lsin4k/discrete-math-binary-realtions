import pytest

from entity import Person


@pytest.fixture
def righhanders():
    return {Person("male"), Person("female"), Person("male"), Person("male")}


@pytest.fixture
def male():
    return Person("male", "Male")

@pytest.fixture
def male1():
    return Person("male", "Male1")

@pytest.fixture
def male2():
    return Person("male", "Male2")

@pytest.fixture
def male3():
    return Person("male", "Male3")


@pytest.fixture
def female():
    return Person("female", "Female")


@pytest.fixture
def female1():
    return Person("female", "Female1")

@pytest.fixture
def female2():
    return Person("female", "Female2")


@pytest.fixture
def female3():
    return Person("female", "Female3")


@pytest.fixture
def dummy():
    class DummyPerson(object):
        pass
    return DummyPerson()


@pytest.fixture
def set_B(male):
    return male

@pytest.fixture
def left_handed():
    return Person("male")
