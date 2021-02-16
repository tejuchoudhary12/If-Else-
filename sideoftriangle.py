s1=int(input("enter side"))
s2=int(input("enter side"))
s3=int(input("enter side"))
if s1==s2==s3:
    print("it is an equlatral triangle")
elif s1==s2 or s2==s3 or s3==s1:
    print("it is scalere triangle")
else:
    print("it is isosceles")
    