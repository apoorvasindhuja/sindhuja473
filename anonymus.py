'''sub=lambda x,y:x*y
print(sub(3,6))
--break--
i=0
while i<10
    i+=1
    if i==5:
        continue
        ''''''
    print(i)'''



def password():
    y=input("enter password:")
    if(y=="xyz"):
        print("login successfully")
    else:
        username()
def username():
    x=input("enter username:")
    if(x=="abc"):
        password() 
    else:
        username()
username()


