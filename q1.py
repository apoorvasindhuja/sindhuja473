x=input("enter a string")
l=x[0]
x=x.replace(l,"$")
x=x.replace("$",l,1)
print(x)
