team=int(input("enter 1st 2nd 3rd team"))
print("Issue? (Y Or N)")
issue=input("enter issue")
if team==1:
    if issue=="N":
        print("1st Team Turn")
    else:
        print("Has Issue So 2nd Team Will Work")
elif team==2:
    if issue=="N":
        print("2nd Team Turn")
    else:
        print("Has Issue Instead of which 3rd team will work")
elif team==3:
    if issue=="N":
        print("3rd Team Turn")
    else:
        print("Has Issue Instead Of which 1st team will Work")
else:
    print("your input is wrong")
    