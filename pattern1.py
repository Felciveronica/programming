n=8
for j in range(1,2*n):
    for i in range(1,n+1):
        if(i>abs(n-j)):
           print("*",end="")
        print(" ",end="")
    print()
      
