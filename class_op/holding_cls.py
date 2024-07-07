
class Holding:
    def __init__(self, name, shares, price, date):
        self.name = name
        self.shares = shares
        self.price = price
        self.date = date

    def cost(self):
        return self.price * self.shares

    def sell(self, nshares):
        self.shares -= nshares

    @classmethod
    def print_table(cls, objects, col_names):
        for col_name in col_names:
            print('{:>10s}'.format(col_name), end=' ')
        print()

        for obj in objects:
            for col_name in col_names:
                print('{:>10s}'.format(str(getattr(obj, col_name))), end=' ')
            print()


if __name__ == '__main__':
    h = Holding('AA', 23, 45.6, '2023-07-08')
    print('Class attribute read h.name ', h.name)
    h.name = 'Modified'
    print('Class attribute set h.name ', h.name)
    # del h.name
    # AttributeError: 'Holding' object has no attribute 'name'
    # print('Class attribute delete h.name ', h.name)

    holdings = [
        Holding('AA', 23, 45.6, '2023-07-08'),
        Holding('IBM', 75, 34.6, '2023-06-08'),
        Holding('IBM', 15, 300.6, '2023-05-01'),
        Holding('MSFT', 15, 151.6, '2023-07-08')
                ]

    Holding.print_table(holdings, ['name', 'price'])

