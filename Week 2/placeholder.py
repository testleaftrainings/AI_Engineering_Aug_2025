def return_numbers():
    return 10, 20

def usepass():
    for i in range(4):
        if (i==3):
            pass
        else:
            print("iterator value is", i)

usepass()

_, num2value = return_numbers()    # Ignoring the first element of the returned pair using a single underscore
print("Value:", num2value)
"""
x,_,y = (1, 2, 3)
print(x, y)   # 1 3
print(type(x))
"""   

