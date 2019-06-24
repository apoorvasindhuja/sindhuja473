'''def display(f):
    f()
def bar():
    print("sindhu")
display(bar)

def avg(x,y):
    return(x+y)/2
def sqrt(x,a):
    return avg(x,x/a)
print(sqrt(5,8))
---req positional---
def add(x,y):
    return x+y
print(add(7,8))
---positional---
def add(x,y):
    return x+y
print(add(5,8))
--keyword--
def add(x,y):
    print(x,y)
    return x+y
print(add(x=23,y=67))
--variable--'''
def add(*x):
    sum=0
    for i in x:
        sum+=i
    return sum
print(add(34,5,67,8))
