# n=[1,2,3,4,5]
# sum=0
# for i in range(len(n)):
#     sum=i+sum
#     print(sum)
#     count=0
# for j in range(1,5):
#     if n%j==0:
#         count=count+1
# if count==2:
#     print(n,"prime number")
# else:
#     print(n,"not prime number")
    
# l=[1,2,3,4,5]
# sum=0
# max=0
# for i in range(len(l)):#i=1
#     for j in range(i+1,len(l)):
#         sum=l[i]+l[j]
#         count=0
#         for k in range(1,sum+1):
#             if (sum%k==0):
#                 count+=1
#         if (count==2 and max<sum):
#             max=sum
# print(max)
                
              
            
        
#find the min ,even product using bitwise      
l=[5,3,4,1,6]
mul=0
s=100000
for i in range(len(l)):
    for j in range(i+1,len(l)):
        mul=l[i]*l[j]
        if(mul&1==0 and mul<s):
                s=mul
print(s)
            
            