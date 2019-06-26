
# decorator: 本质上，decorator就是一个返回函数的高阶函数
# def log(func):
#     def wrapper(*args, **kwargs):
#         print('i am log')
#         func(*args, **kwargs)
#     return wrapper
#
# @log
# def now():
#     print('2019-00')

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')