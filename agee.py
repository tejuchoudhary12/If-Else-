age=int(input("enter age"))
if age<2:
    print("person is baby")
elif age>=2 and age<4:
    print("person is toddler")
elif age>=4 and age<13:
    print("person is kid")
elif age>=13 and age<20:
    print("person is teenager")
elif age>=20 and age<65:
    print("person is an adult")
elif age>65 and age<=150:
    print("person is elder")
else:
    print("insufficent age")