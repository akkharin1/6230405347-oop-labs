class Student:
    university_name = ("Khon kaen university")

    def __init__(self, name, *course_ids):
        self.name = name
        self.course_ids = course_ids

    def print(self):
        print("{} registered courses {}".format(self.name, self.course_ids))


if __name__ == "__main__":
    manee = Student("Manee", "842004")
    mana = Student("Mana", "842004", "842005", "813701")
    chujai = Student("Chujai", "842004", "842005")
    manee.print()
    mana.print()
    chujai.print()
    print(f'These students are in {Student.university_name}')