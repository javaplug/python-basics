share_price = {
    'IBN': 23.4,
    'AA': 26.2,
    'YAHOO': 12
}
print('IBN' in share_price)  # prints true if the collection has the given key

inputs = [{'1': 1}, {'2': 2}]
# filtering data in list/dict

criteria = '1'
output_one = list(filter(lambda dict_data: criteria in dict_data, inputs))
# [{'1': 1}]
print(output_one)

numbers = [1, 2, 3, 4]
chars = ['1', '2', '3', '4']
# alpha_numeric = {k: v for k, v in zip(numbers, chars)}
alpha_num_dict = dict(zip(numbers, chars))
# {1: '1', 2: '2', 3: '3', 4: '4'}
print(alpha_num_dict)

alpha_numeric = [{k: v} for k, v in zip(numbers, chars)]
# [{1: '1'}, {2: '2'}, {3: '3'}, {4: '4'}]
print(alpha_numeric)
