
def get_name(name='kerwin', *args, **kwargs):
    print(name, args)

get_name('bob', 2, 4)

# recursive function, default 100
i = 1
sum = 0
def get_result(i):
    global sum
    if (i < 5):
        # print(type(i))
        sum = sum + i
        get_result(i+1)
    else:
        print(sum)
        # return sum
get_result(1)

def fb(n):
    if n < 1:
        return '-1'
    elif n == 1 or n == 2:
        return 1
    else:
        return fb(n - 1) + fb(n - 2)
print(fb(20))