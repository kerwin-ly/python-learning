init_list = ['kerwin', 'bob', 'john']

# append data in the end
init_list.append('david') # ['kerwin', 'bob', 'john', 'david']

# remove the last of data, return the data
init_list.pop()

# insert data in which index
init_list.insert(1, 'david') # ['kerwin', 'david', 'bob', 'john']

# get length
len(init_list)

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
