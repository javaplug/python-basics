def typed_property(name, expected_type):
    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop


Integer = lambda name: typed_property(name, int)
Float = lambda name: typed_property(name, float)


class Holdings:
    shares = Integer('shares')
    prices = Float('prices')

    def __init__(self, name, shares, prices):
        self.name = name
        self.shares = shares
        self.prices = prices


if __name__ == '__main__':
    h = Holdings('IBM', 25, 4.1)
    print(f'{h.name} cost : {h.shares * h.prices}')
    # h.shares = '10'  # TypeError: Expected <class 'int'>
