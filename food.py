print("FOODIE RESTAURANT")
print("Menu")
print("1.VEG")
print("2.NON-VEG")
print("3.SEA")
print("4.soft drink")
print("5.junk food")
print("6.ICE-CREAMS")
food=int(input("select any one option="))
#veg:
if food==1: 
     print("HELLO CUSTOMER YOU SELECTED! *VEG* ")
     print("Natures Best-- YOU Must Try Veg itmes")
     print("1,paneer butter masala--cost-200")
     print("2,aloo gobi--cost-100")
     print("3,veg-biriyani--cost-400")
     items=int(input("select items"))
     if items==1:
      print("Paneer butter masala")
      print("Thank you customer..! you order paneer butter masala")
     elif items==2:
      print("Aloo gobi")
      print("Thank you customer..! you order paneer aloo gobi")
     elif items==3:
      print("Veg-Biriyani")
      print("Thank you customer..! you order paneer veg-biriyani")
     print("THANKS FOR ORDER VISIT AGAIN")
#non veg:
elif food==2: 
     print("HELLO CUSTOMER YOU SELECTED! *NON-VEG* ")
     print("Natures Best-- YOU Must Try Non-Veg itmes")
     print("1,Mutton Biriyani--cost-400")
     print("2,Chicken Biriyani--cost-300")
     print("3,Chicken Tikka--cost-200")
     nonveg=int(input("select items"))
     if nonveg==1:
      print("Mutton Biriyani")
      print("Thank you customer..! you order mutton biriyani")
     elif nonveg==2:
      print("chicken biriyani")
      print("Thank you customer..! you order chicken biriyani")
     elif nonveg==3:
      print("chicken tikka")
      print("Thank you customer..! you order paneer chicken tikka")
     print("THANKS FOR ORDER VISIT AGAIN")
     
#sea food:
elif food==3:
     print("HELLO CUSTOMER YOU SELECTED! *SEA FOOD* ")
     print("Natures Best-- YOU Must Try sea food items")
     print("1,fish biriyani--cost-800")
     print("2,prawns biriyani--cost-600")
     print("3,crab biriyani--cost-900")
     sea=int(input("select items"))
     if sea==1:
      print("fish biriyani")
      print("Thank you customer..! you order fish biriyani")
     elif sea==2:
      print("prawns biriyani")
      print("Thank you customer..! you order prawns biriyani")
     elif sea==3:
        print("crab biriyani")
        print("Thank you customer..! you order crab biriyani")
        print("THANKS FOR ORDER VISIT AGAIN")
#soft drinks:      
elif food==4:
     print("HELLO CUSTOMER YOU SELECTED! *SOFT DRINK* ")
     print("Natures Best-- YOU Must Try soft drink")
     print("1,pepsi-->cost-90")
     print("2,coco-cola-->cost-80")
     print("3,thumbsup-->cost-120")
     softdrink=int(input("select items"))
     if softdrink==1:
      print("pepsi")
      print("Thank you customer..! you order pepsi")
     elif softdrink==2:
      print("coco cola")
      print("Thank you customer..! you order coco cola")
     elif softdrink==3:
        print("thumbsup")
        print("Thank you customer..! you order thumbsup")
        print("THANKS FOR ORDER VISIT AGAIN")
#junk food:
elif food==5:
     print("HELLO CUSTOMER YOU SELECTED! *JUNKFOOD* ")
     print("Natures Best-- YOU Must Try Junk food itmes")
     print("1,Bugger--cost-800")
     print("2,pizza--cost-100")
     print("3,french fries--cost-400")
     junk=int(input("select items"))
     if junk==1:
      print("bugger")
      print("Thank you customer..! you order bugger")
     elif junk==2:
      print("2,pizza")
      print("Thank you customer..! you order pizza")
     elif junk==3:
        print("3,french fries")
        print("Thank you customer..! you order french fries")
        print("THANKS FOR ORDER VISIT AGAIN")
#ice cream
elif food==6:
     print("HELLO CUSTOMER YOU SELECTED! *ICE-CREAMS* ")
     print("Natures Best-- YOU Must Try ice-cream")
     print("1,Butterscotch--cost-120")
     print("2,Black current--cost-100")
     print("3,Green pista--cost-400")
     ice=int(input("select items"))
     if ice==1:
      print("Butterscotch")
      print("Thank you customer..! you order Butterscotch")
     elif ice==2:
      print("Black current")
      print("Thank you customer..! you order Black current")
     elif ice==3:
        print("Green pista")
        print("Thank you customer..! you order Green pista")
        print("THANKS FOR ORDER VISIT AGAIN")
