# A Sample class with init method
class Person:
    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def invite(self):
        print('Welcome', self.name)


# Creating different objects
p1 = Person('Mani')
p2 = Person('Ram')
p3 = Person('Sita')

p1.invite()
p2.invite()
p3.invite()