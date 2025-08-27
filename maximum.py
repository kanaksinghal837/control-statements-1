a = int(input("Enter a value:"))
b= int(input("Enter b value:"))
c= int(input("Enter c value:"))
if((a>b) & (a>c)):
    print(a,"is Greatest")
elif((b>a) & (b>c)):
    print(b,"is Greatest")
else:
    print(c, "is Greatest")