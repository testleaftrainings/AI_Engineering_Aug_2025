import base2 as b
print("base2 imported")
print(b.__doc__)

def addfun():
    c=b.add(5,6,7)
    print(c)

addfun()
print("Inside child", __name__)


