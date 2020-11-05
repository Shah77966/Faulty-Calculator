#Faulty calculator
while(1):
    c = input("Enter operation + - % /")
    if (c=="+" or c=="-" or c=="*" or c=="/" or "%"):
        a = int(input("Enter first number"))
        b = int(input("Enter second number"))
        if a==45 and b==3 and c=='*':
            print("555")
        elif a==56 and b==9 and c=='+':
            print("77")
        elif a==56 and b==6 and c=='/':
            print("4")
        elif c=="+":
            print("sum is:", a+b)
        elif c=="-":
            print("sub is :", a-b)
        elif c=="*":
            print("multiplication is :", a*b)
        elif c=="/":
            print("Division is :",a/b)
        elif c=="%":
            print("mod id: ", a%b)
    else:
         break