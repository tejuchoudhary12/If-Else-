user=int(input("ente rno."))
if user%5==0 and user%11==0:
    print("It Is Divisible By Both")
elif user%5==0 or user%11==0:
    print("Divisible by one", "Which one")
    if user%5==0:
        print("By 5")
    else:
        print("by 11")
else:
    print("not divisible")