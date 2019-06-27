
# Anonymous function: lambda
# 'x' => param
print(list(map(lambda x: x * x, [1, 2, 3])))

# named function
# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))

# lambda
L = list(filter(lambda n: n % 2 == 0, range(1, 20)))
print(L)

func = lambda x: x + 1
print(func(1))