"""This is an class exercise"""
def add(*args):
    print("Arguments received = :",args)
    sum=0
    for i in args :
        sum+=i #sum=sum+i
    return sum
    
#d = add(20,10,20,10)
#print("Sum is = ",d)

if (__name__ == "__main__"):
    print("Running Mainly base2.py")
    print(__doc__)
else:
    print("imported module")
    print(__name__)