
# issubclass(class, classinfo): to check if class extends classinfo(tuple), class is child class
class A():
    pass
class B(A):
    pass
print(issubclass(B, A)) # True

# hasattr
class C():
    def __init__(self):
        self.name = 'kerwin'
c = C()
print(hasattr(c, 'name')) # True

# getattr
print(getattr(c, 'age', 'not get attribute name'))

# setattr
setattr(c, 'age', 23)
print(c.age)

# delattr
delattr(c, 'age')