x=[1,2,3,4,5]
y=[]
for i in x:
    if(i%2==0):
        y.append(i)
print(y)

list3=[i for i in x if i%2==0]
print(list3)

