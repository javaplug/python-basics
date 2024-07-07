import class_op.inheritence_op.parent as p


class ChildNewConstructor(p.Parent):
    def __init__(self, value, ext_value):
        self.ext_value = ext_value
        super().__init__(value)

    def use_new_value(self):
        print('from Child new constructor.use_new_value ', self.ext_value)

