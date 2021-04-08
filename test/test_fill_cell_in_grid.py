from ui import fill_grid_


def fill_cell(param):
    global fill_cell_had_been_called
    fill_cell_had_been_called += 1


def test_fill_cell_in_grid(male, male1, male2, female, female1, female2):
    global fill_cell_had_been_called
    fill_cell_had_been_called = 0

    relations = {(male, male), (male1, female), (female1, male)}
    fill_grid_(fill_cell, relations)
    assert fill_cell_had_been_called == 3

    fill_cell_had_been_called = 0

    relations = {}
    fill_grid_(fill_cell, relations)
    assert fill_cell_had_been_called == 0
