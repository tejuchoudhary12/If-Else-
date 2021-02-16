girls=int(input("enter the no.of girls"))
if girls==12:
    print("room is occupied")
elif girls<=12:
    print(12-girls, "more girls should be added ")
else:
    print(girls-12,"girls shift them to other room")