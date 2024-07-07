import class_op.inheritence_op.parent as p


class ChildNewMethod(p.Parent):

    def new_method(self):
        print('from Child.new_method')
        super().grok()
