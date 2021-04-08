from controller import cast_to_persons


class TwoGroups:
    A: set
    B: set

    def __init__(self, left_handed, right_handed):
        self.A = left_handed
        self.B = right_handed

    def cast_to_persons(self):
        self.A = cast_to_persons(self.A)
        self.B = cast_to_persons(self.B)
        return self