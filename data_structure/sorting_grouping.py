shares = [
    {'name': 'AA', 'price': 10.3, 'shares': 23, 'date': '2023-4-5'},
    {'name': 'IBM', 'price': 5.3, 'shares': 3, 'date': '2023-4-5'},
    {'name': 'IBM', 'price': 25.3, 'shares': 10, 'date': '2024-4-5'},
    {'name': 'MSFT', 'price': 70.3, 'shares': 50, 'date': '2023-4-5'}
]

print('Sorted by Name')
shares.sort(key=lambda s: s['name'])
print(shares)

print('Minimum share')
print(min(shares, key=lambda m: m['shares']))

print('Maximum price')
print(max(shares, key=lambda mx: mx['price']))


import itertools
print('Grouping by Name')
share_grp = itertools.groupby(shares, key=lambda n: n['name'])
for share_name, dtl in share_grp:
    print(share_name)
    for item in dtl:
        print(item)

