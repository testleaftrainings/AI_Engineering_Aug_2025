num=6
c=5


def add(a):
    #global c
    globals()["c"]=a+num
    #c=a+c
    print("C Inside =",c)   
    return c

print("C before Modification=",c)
d=add(5)

print("D = ",d)
print("C Outside=", c)
