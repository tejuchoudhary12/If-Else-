alphabate=input("enter alphabate")
symbol=input("enter specail symbol")
number=int(input("enter no."))
if alphabate>="A" and alphabate<="Z":
    print("move further")
else:
    print("Try alphabate")
if symbol=="#" or symbol=="@" or symbol=="_":
    print("move Further")
else:
    print("chose wisely")
if number>1 and number<100:
    print("streong password")
    print(alphabate+symbol+str(number))
else:
    print("try again")

