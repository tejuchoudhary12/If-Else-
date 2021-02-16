side1=int(input("enter side1"))
side2=int(input("enter side2"))
side3=int(input("enter side3"))
if side1+side2>side3 or side2+side3>side1 or side1+side3>side2:
    print("triangle is vaild ")
else:
    print("triangle is not vaild ")
