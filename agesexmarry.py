age=int(input("Enter your age"))
print("sex? (M or F)")
sex=input("Enter your sex")
print("Married? (Y or N)")
married=input("Enter your status")
if sex=="F" and age>=20 and age<=60:
    print("Work in Urban area only")
elif sex=="M" and age>=20 and age<=40:
    print("Work anywhere")
elif sex=="M" and age>40 and age<=60:
    print("Urban areas only")
else:
    print("ERROR")
    