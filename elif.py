#review 
review=int(input("enter a review="))
if(10>=review>8):
    print("5 star")
elif(8>=review>6):
    print('4 star')
elif(6>=review>5):
    print("3 star")
elif(5>=review>3):
    print("2 star")
elif(3>=review>1):
    print("1 star")
else:
    ("empty")

#digital billing
print("FOODIE RESTAURANT")
print("Menu")
print("1.VEG")
print("2.NON-VEG")
print("3.SEA")
food=int(input("select your  menu"))
if food==1:
    print("veg items","paneer butter masala")
    print("amount-200")
    print("THANKS FOR ORDER VISIT AGAIN")
elif food==2:
    print("non veg","chiken biriyani")
    print("amount-400")
    print("THANKS FOR ORDER VISIT AGAIN")
elif food==3:
    print("sea","fish fry")
    print("amount=500")
    print("THANKS FOR ORDER VISIT AGAIN")
else:
    print("sorry inavalid food item")
        
    
    

