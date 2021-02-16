salary=int(input("enter your salary"))
if salary<=10000:
    print(salary*0.2,"HRA")
    print(salary*0.8,"DA")
    print(salary+salary*0.2+salary*0.8)
elif salary<=20000:
    print(salary*2.5,"HRA")
    print(salary*0.9,"DA")
    print(salary+salary*2.5+salary*0.9)
elif salary>10000:
    print(salary*0.3,"HRA")
    print(salary*9.5,"DA")
    print(salary+salary*0.3+salary*9.5)