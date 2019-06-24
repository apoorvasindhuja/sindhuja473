x=input("enter a string:")
if(len(x) < 2):
  print("empty string")
  if(len(x) == 2):
      print(x*2)
else:
    print(x[0],x[1],x[-2],x[-1])
