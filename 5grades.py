phy=int(input("enter phy marks"))
chmstry=int(input("enter chmstry marks"))
bio=int(input("enter bio marks"))
math=int(input("enter math marks"))
computer=int(input("enter computer marks"))
sum=phy+chmstry+bio+math+computer
per=sum/500*100
if per>=90:
    print("A")
elif per>=80:
    print("B")
elif per>=70:
    print("C")
elif per>=60:
    print("D")
elif per>=50:
    print("E")
elif per>=40:
    print("F")
else:
    print("needs to work hard more")
