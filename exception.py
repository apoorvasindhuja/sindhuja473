'''a=int(input("enter a value"))
b=int(input("enter b value"))
dict={"name":"sindhu"}
try:
    print(a/b)
    print(dict['branch'])
except ZeroDivisionError as z:
    print("hi:",z)
except (NameError,KeyError):
    print("not found")
else:
    print('crct input')
finally:
    print("hello")'''
a=input("enter 1st string:")
b=input("enter 2nd string:")
try:
    raise TypeError("mul cannot perform")
    print(a/2)
    print(a*b)
except:
    print("exception:")
