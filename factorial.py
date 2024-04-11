def fact(x):
    if x<0:
        print(0)
    elif x==1 or x==0:
        print("x=1")
    else:
        n=1
        while(x>1):
            n=n*x
            x=x-1
        return n
    
# comment

    