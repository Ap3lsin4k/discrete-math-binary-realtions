from entity import Person


def dummy_job():
    raise AssertionError()


spy_job_was_called = False


def spy_job():
    global spy_job_was_called
    spy_job_was_called = True


def test_sex_male():
    p = Person("male")
    assert p.sex == "male"
    p.do_job_based_on_sex(spy_job, dummy_job)
    assert spy_job_was_called == True


def test_sex_female():
    p = Person("female")
    assert p.sex == "female"
    global spy_job_was_called
    spy_job_was_called = False
    p.do_job_based_on_sex(dummy_job, spy_job)
    assert spy_job_was_called