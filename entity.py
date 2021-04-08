class Person:
    sex: str

    def __init__(self, sex="female", name="No name"):
        self.sex = sex
        self.bachelor = True
        self.name = name
        self.id = -1
        self.son_in_law = False

    def do_job_based_on_sex(self, job_for_males, job_for_females):
        if self.sex == "male":
            job_for_males()
        elif self.sex == "female":
            job_for_females()
        else:
            raise ValueError("Check the spelling for sex property.")

    # one to many
    def can_be_father_in_law_of(father_in_law, son_in_law):
        return father_in_law.sex == "male" and son_in_law.sex == "male" \
               and father_in_law is not son_in_law

    # one to one
    def can_be_husband_of(husband, wife):
        return husband.sex == "male" and wife.sex == "female" \
                and husband.bachelor and wife.bachelor

    def generate_father_in_law_relation(self, other, out_relation):
        if self.can_be_father_in_law_of(other) and not other.son_in_law:
            out_relation.add((self, other))
            other.son_in_law = True

    def generate_husband_relation(self, possible_wife, out_relation):
        if self.can_be_husband_of(possible_wife):
            out_relation.add((self, possible_wife))
            self.bachelor = False
            possible_wife.bachelor = False