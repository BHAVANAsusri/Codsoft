c=0
a=0
b=0
print ("""    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    5.Exponents""")

while(c<1000):
    print("")
    var1=int(input("choose an operation to be performed:"))
    
    if var1==1 or var1==2 or var1==3 or var1==4 :
        a=(float(input(" Enter Number1:")))
        b=(float(input("Enter Number 2:")))
        if var1==1:
            print(a+b)
        elif var1==2:
            print(a-b)
        elif var1==3:
            print(a*b)
        elif var1==4:
            print(a/b)
        else:
            print("Invalid Number")
    elif  var1==5:
        i=0
        n=0
        i=float(input("Enter the base value:"))
        n=float(input("Enter the power value:"))  
        ch=i**n
        print(" tha value is ",ch)
    else:
        print("Invalid Number")
