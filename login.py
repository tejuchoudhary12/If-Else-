name=input("Enter you name: ")
password=input("Enter your password: ")
if name=="tejuchoudhary":
    if password=="TEJU12":
        print("Successful Login")
    else:
        print(name,password,"You have entered incorrect password or name")
        name1=input("Enter you name: ")
        if name=="tejuchoudhary":
            password=input("Enter your password: ")
            if password=="TEJU12":
                print("Successful Login")
            else:
                print("wrong password entered")
        else:
            print("Again entered wrong name")
else:
    print("Wrong details entered")


