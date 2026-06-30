
# #arthematic comperhensive:
# n=int(input("enter a value="))
# l=[val+10 for val in range(n)]
# l1=[val-10 for val in range(n)]
# l2=[val*10 for val in range(n)]
# l3=[val%10 for val in range(n)]
# l4=[val/10 for val in range(n)]
# l5=[val//10 for val in range(n)]
# print(l1,l2,l3,l4,l5,)

# #even comperhensive:
# m=5
# n=[val for val in range(1,m+1) if(val%2==0)]
# print(n)

# #odd comperhensive:
# v=7
# u=[val for val in range(1,v+1) if(val&1==1)]
# print(u)

# #position of the even odd:
# k=9
# m=["even" if(val%2==0) else "odd" for val in range(1,9)]
# print(m)

# #negitive positive
# l=[1,-2,-3,-4,5,7,8,9,10]
# neg=[]
# pos=[]
# l2=[neg.append(val) if val<=0 else pos.append(val) for val in l]
# print(neg)
# print(pos)

s="hi hello ravi garu"
vow=([i for i in s if i.lower() in "aeiou"])
con=([i for i in s if i.isalpha() and i.lower() not in "aeiou"])
print(vow)
print(con)
