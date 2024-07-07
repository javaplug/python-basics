name = 'sakthivel_thangaraj'
print(f'First name is {name[:name.rfind('_')]}')

# converting number to string
numbers = ['1', '2', '3', '4', '2', '2']
criteria = 2
filtered_num = [i for i in numbers if i == str(criteria)]
print(filtered_num)


