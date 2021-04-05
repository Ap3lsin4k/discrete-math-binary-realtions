def load_saved_sets():
    f1 = open(r"Set A.txt", "r", encoding="UTF-8")
    right_handed_people = f1.read().split(" ")
    right_handed_people = right_handed_people[:-1]  # remove '' after split
    f2 = open(r"Set B.txt", "r", encoding="UTF-8")
    left_handed_people = f2.read().split(" ")
    left_handed_people = left_handed_people[:-1]
    return left_handed_people, right_handed_people


def save_relation_to_file(name, relation_itself):
    with open(str(name)+".txt", "w", encoding="UTF-8") as f:
        for i in relation_itself:
            f.write(str(i))