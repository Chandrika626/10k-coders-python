# s=input("enter a char=")
# if('A'<=s<='z'):
#     print(s,"upper case")
# else:
#     print(s,"not upper case")
    
    
# s=input("enter a digits")
# if('0'<=s<='9'):
#     print(s,"digits")
# else:
#     print(s,"not digit")   
 
# ch=input("enter a char")
# if '0'<=ch<='9':
#     print(ord(ch),ch)
    
# ch=str(input("enter a dig"))
# if 'A'<=ch<='Z':
#     print(chr(ch),ch)  


# l=['a','s','d','e']
# l.append(['kavya'])
# print(l)

# ch=input("enter a digit")
# if('0'<=ch<='9',):
#     print(ch,+1)

# ch=input("enter a char")
# if 'A'<=ch<='z' or 'a'<=ch<='z':
#     print(ch,chr(ord(ch))-32)
    
    
# import random
# secret=random.randint(1,20)
# guess=52
# print("welcome to guess")
# while guess!=secret:
#     guess=int(input("enter a value"))
#     if guess==secret:
#         print("you won a game")
#         break
#     elif guess<=secret:
#         print("too low")
#     else:
#         print(" too high")


import random
password="chandrika"
guess="chandu"
print("singin")
while guess!=password:
    guess=str(input("enter a password"))
    if guess==password:
        print("sign in is done ")
    else:
        print("is not done")