num1=int(input("enter the no.1"))
opr=input("enter the oprator")
num2=int(input("enter the no.2"))
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
elif opr=="//":
    print(num1//num2)
elif opr=="%":
    print(num1%num2)
else:
    print("invaild")