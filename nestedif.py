alpha=input("Enter any character")
spcl=input("Enter any special character")
number=int(input("Enter any number"))
if alpha=="S" or alpha=="M" or alpha=="P" or alpha=="J" or alpha=="T":
    if spcl=="@" or spcl=="#" or spcl=="_":
        if 1<number and 1000>number:
            print(alpha+spcl+str(number))
        else:
            print("Write number within 1 to 1000")
    else:
        print("Enter @ # _")
else:
    print("Enter A,B,C,D,E")