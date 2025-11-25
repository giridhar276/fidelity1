# fixed arguments
def display(a,b):
    print(a,b)
display(10,20)

# default arguments
def display(a =0,b = 0,c= 0):
    print(a,b,c)

display()
display(10)
display(10,20)
display(10,20,30)

## keyword arguments
def display(c,a,b):
    print(a,b,c)
display(b=20,c=30,a=10)

# variable length arguments
def display(*args):
    #print(args)
    for val in args:
        print(val)
display(10,20,30,40,50,60,70,80,90,100)