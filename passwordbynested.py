alphabate=input("Enter any alphabate")
symbol=input("enter any symbol or character")
number=int(input("Enter any number"))
if alphabate>="A" and alphabate<="Z":
    if symbol=="#" or symbol=="@" or symbol=="_":
        if number>1 and number<100:
            print(alphabate+symbol+str(number))
        else:
            print("try  again")
    else:
        print("enter ant of this @ # _")
else:
    print("write only one capital letter")
