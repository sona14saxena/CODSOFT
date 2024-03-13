def calculator():
    a=int(input("Enter no 1:"))
    b=int(input("Enter no 2:"))
    choice=input("Pick from +,-,*,/,%")
    if choice =="+":
        result=a+b
        print("addition of two no is:",result)
    elif choice=="-":
        result=a-b
        print("subtraction of two no is :",result)
    elif choice=="*":
        result=a*b
        print("product of two no is :",result)
    elif choice=="/":
        result=a/b
        print("division of two no is:",result)
    elif choice=="%":
        result=a%b
        print("modulus of two no is :",result)
    else:
        print("wrong choice")
calculator()
    
