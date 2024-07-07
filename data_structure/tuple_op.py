
# Creating a tuple
input = ('IBN', 5, 23.6)

# unpacking tuple
share_name, count, price = input

# total_share_cost = input[1] * input[2]
total_share_cost = count * price
print('Total Share cost : ', total_share_cost)

# tuples are immutable
# input[1] = 6
# TypeError: 'tuple' object does not support item assignment

def test_tuple():
    print(inputs)
    for name, age in inputs:
        print(name, ' is ', age, ' years old')


inputs = [('Abi', 27), ('Abi', 24), ('1', 27), ('Ragu', 26)]
inputs.sort()
# [('1', 27), ('Abi', 24), ('Abi', 27), ('Ragu', 26)]
print(inputs)


# numbers = [23,4,6,6]
# numbers.sort()
# numbers.sort(reverse=True)
# sorted_list=[]
# for i in numbers:
#     if(i<=(i+1)):



# test_tuple()
# print(numbers)
