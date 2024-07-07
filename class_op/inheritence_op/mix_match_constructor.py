
class Father:

    def __init__(self, father_name):
        self.father_name = father_name

    def print_parent_name(self):
        print('Father Name is ', self.father_name)


class Mother:

    def __init__(self, father_name, mother_name):
        self.mother_name = mother_name
        super().__init__(father_name)

    def print_parent_name(self):
        print('Mother name is ', self.mother_name)
        super().print_parent_name()


class Child(Mother, Father):
    pass


child = Child('sakthi', 'saran')
child.print_parent_name()

