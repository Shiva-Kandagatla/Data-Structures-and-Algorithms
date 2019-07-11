n = int(input("Enter Height : "))
sp=" "
st="*"
if n==1:
    print(st)
else:
    temp = n
    print(sp*(n-1) , end="")
    print(st*n)
    x=n-2
    for i in range(n-2):
        print(sp*x,end="")
        print(st,end="")
        print(sp*(n-2) , end="")
        print(st)
        x=x-1
    print(st*(n) , end="\n")    

