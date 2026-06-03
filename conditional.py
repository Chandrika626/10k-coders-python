#positive or not
score=(int(input("enter a value")))
if(score>=0):
    print("score is a positive")
else:
    print("score is not positive")
    
#upper case or lower case
name=(str(input("enter a letter")))
if(name>='A'and name<='Z'):
    print("upper case letter")
else: 

    print(" lower case letter")

#pass or fail
Math=(int(input("enter a sub1")))
Social=(int(input("enter a sub2")))
PS=(int(input("enter a sub3")))
English=(int(input("enter a sub4")))
Telugu=(int(input("enter a sub5")))
Hindi=(int(input("enter a sub6")))
if(Math>=35 and Social>=35 and PS>=35 and English>=35 and Telugu>=35 and Hindi>=35):
    print("pass all subject")
else:
    print("fail")
    