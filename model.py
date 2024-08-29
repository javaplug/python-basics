
class Typed:
    expected_type = object

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class Holding:
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.price * self.shares


if __name__ == '__main__':
    h = Holding('IBM', 25, 34.5)
    print(f'Share {h.shares} : cost : {h.cost}')
    # h.price = '24'   # TypeError: Expected <class 'float'>
    # h.shares = 'a lot'  # TypeError: Expected <class 'int'>
    h.shares = 26
    print(f'After change: share {h.shares} : cost : {h.cost}')

    # t = Integer('test')
    # t = 4   # This would override the existing reference
    # this would work only inside class

    h.append


