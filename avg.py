x=int(input("enter the x marks"))
y=int(input("enter the y marks"))
z=int(input("enter the z marks"))
avg=(x+y+z)/3
if avg>75:
    print("A grade")
  elif (65>=avg<=75):
        print("B grade")
    elif (35>=avg<=65):
             print("C grade")
        else:
            print("fail")
