card=input("Insert your card")
language=input("Enter your language")
account=input("Enter your account name")
pin =int(input("Enter your pin number"))
amount=int(input("Enter number of amount you have to withdraw"))
balance=10000
if card=="pinside" :
    if language=="english" or language=="hindi" or  language=="marathi":
        if account=="sharing" or "current":
            if pin==1210:
                if balance<=10000:
                    print("Prosses Successfully Done")
                else:
                    print("insufficeint amount is been entered")
            else:
                print("Wrong pin entered")
        else:
            print("Invaild account is been entered")
    else:
        print("Language is been not found")
else:
    print("Invaild")
