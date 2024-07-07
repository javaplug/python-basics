
class Parent1:

    @staticmethod
    def parent1_method():
        print('Parent1 method')


class Parent2:

    @staticmethod
    def parent2_method():
        print('Parent2 method')


class CombineParent(Parent1, Parent2):
    pass


combineParent = CombineParent()
combineParent.parent1_method()
combineParent.parent2_method()


