n=int (input("Enter number"))
count=0
i=1
while(i<=n):
    if (n%i==0) :
        count=count+1;
    i=i+1
if (count==2) :
     print (i-1,"is a Prime number.")
else :
     print (i-1, "is not Prime number.")
    
