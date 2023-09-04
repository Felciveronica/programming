def gcd(x,y):
    if(x>1 and y>1):
        if(x>y):
          x,y=y,x
          print(x,"  " ,y)
        if(y%x==0):
            return x
        else:
              
            return gcd(x,y%x)
    else:
        return 1
print(gcd(32,14))


 

