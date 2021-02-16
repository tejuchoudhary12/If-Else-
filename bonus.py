salary=int(input("enter salary"))
years=int(input("enter years"))
if years>10:
    print(10/100*salary)
elif years>=6 and years<=10:
    print(8/100*salary)
elif years<6:
    print(5/100*salary)