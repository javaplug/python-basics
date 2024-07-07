names = ['Ram', 'Sam', 'Ravi']

for name in names:
    print('Iteration : ', name)

names.sort()
print('Sorted names : ', names)

names.append('Raju')
names.insert(1, 'John')
print('Printing collection (after modification) : ', names)

# Check if exists
print('Ram exists in collection : ', 'Ram' in names)

inputs = [{'name': 'Ravi', 'age': 32}, {'name': 'Abu', 'age': 28}]
inputs.sort(key=lambda c: c['name'], reverse=False)
print('Printing sorted collection ', inputs)
