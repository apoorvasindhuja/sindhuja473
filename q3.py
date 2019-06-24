x=input("enter a string:")
y='ing'
z='ly'
if len(x)<3:
    print(x)
else:
    if x.endswith('ing'):
        print(x+z)
    else:
        print(x+y)
        
    
    
