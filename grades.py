marks=int(input("enter no."))
if marks>90:
    print("A")
elif marks>80 and marks<=90:
    print("B")
elif marks>=60 and marks>40:
    print("C")
elif marks<60 and marks>40:
    print("D")
else:
    print("FAIL")
    