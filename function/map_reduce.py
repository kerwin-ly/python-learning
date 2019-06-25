from functools import reduce

def multiple(x):
    return x * x + 100

# map: abstract formula with a function
map_num = map(multiple, [1, 2, 3, 4])
print(list(map_num)) # 1, 4, 9, 16


# reduce: use the function result to calculate
def transfer(x, y):
    return x * 10 + y

print(reduce(transfer, [1, 2, 3, 4])) # 1234

