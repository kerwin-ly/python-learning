init_list = ['kerwin', 'bob', 'john']
num_list = [1, 2, 3]
str = 'kerwin'

# slice
print(num_list[1:2]) # 2
print(num_list[:]) # [1, 2, 3]
print(num_list[-1:]) # [3]
print(str[:2]) # 'ke'

# get index and value
for index, value in enumerate(num_list):
    print(index, value)

# append data in the end
init_list.append('david') # ['kerwin', 'bob', 'john', 'david']

# merge two lists
init_list.extend(num_list)
# print(init_list)

# remove the last of data, return the data
init_list.pop()

# insert data in which index
init_list.insert(1, 'david') # ['kerwin', 'david', 'bob', 'john']

# get length
len(init_list)

# generator
g = (x * x for x in range(10))
for i in g:
    print(i)

# tuple: after init tuple, you can not update the data in it.
init_tuple = (22, 33, 44)

# loop
for name in init_list:
    print(name)

# range(x)
sum = 0
for x in list(range(5)): # [0, 1, 2, 3, 4]
    sum += x
print(sum) # 10

# generate a tuple which length is 1(have to add comma in the end, otherwise the result will be number 1)
tuple_first = (1,) # (1, )
num = (1) # 1
