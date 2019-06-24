x=range(1,50)
for i in x:
    if i%3==0:
        print("fizz")
        if i%5==0:
            print("buzz")
            if i%3==0 & i%5==0:
                print("fizzbuzz")
    else:
        print(i)
