day=input("Enter Day")
meal=input("What you want Breakfast, Lunch or Dinner")
if day=="monday":
    if meal=="breakfast":
        print("Poori Bhazi")
    elif meal=="lunch":
        print("Sambhar Rice")
    elif meal=="dinner":
        print("Chicken Rice")
elif day=="tuesday":
    if meal=="breakfast":
        print("Poha")
    elif meal=="lunch":
        print("Paneer Roti")
    elif meal=="dinner":
        print("Dal Rice")
elif day=="wednesday":
    if meal=="breakfast":
        print("Upma")
    elif meal=="lunch":
        print("Loky Roti")
    elif meal=="dinner":
        print("Kofta Rice")
else:
    print("We are sorry...\nOur hotel is closed today")
