
class Turtle():
    def __init__(self, num):
        self.num = num

class Fish():
    def __init__(self, num):
        self.num = num

class Pool:
    def __init__(self):
        self.turtle = Turtle(5)
        self.fish = Fish(10)

pool = Pool()
print('There are %d turtles and %d fishes in pool' %(pool.turtle.num, pool.fish.num))