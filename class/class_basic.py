
# basic class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # private name, add underline '__' before property/function
        __code = '007'

    def get_age(self):
        print(self.age)

    def get_code(self):
        return self.__code


p = Person('kerwin', 24)
p.get_age()
# p.__code # error occured, you cannot get private property

# extends
class Man(Person):
    pass

m = Man('bob', 29)
m.get_age()