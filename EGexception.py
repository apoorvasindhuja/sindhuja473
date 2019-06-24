class abc(Exception):
    a=int(input("enter a value"))
    b=int(input("enter b value"))
try:
    raise abc("exception")
    print(a/b)
except:
    print("default")
