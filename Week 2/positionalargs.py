def add(*args):
    print("Argument Received", args)
    sum=0
    for i in args:
        print("Args :" ,i)
        sum+=i
        print("Cumm add =", sum)
    return sum

d=add(5,6,7)
print("The sum Value =", d)