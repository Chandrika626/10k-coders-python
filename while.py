n=123
sum=0 #0--3 /3---32 /32-321
while(n>0): #123>0---->/12>0--->/1>0--1
       temp=n%10 #123%10=3----->/12%10=2---->/1%10=1
       sum=(sum*10)+temp #(0*10)+3=3---->/(3*10)+2=32--->/(32*10)+1=321
       n=n//10 #123//10=12 --->/12//10=1--->/1//10=0
       print(sum)

num = 7
original = num
count = 0
while num > 0:
    digit = num % 10
    if original % digit == 0:
        count += 1
        num //= 10
print(count)

n=1248
count=0
while(n>0):
     temp=n%10
     if temp!=0 and n%temp==0:
         count+=1
     n//=10
print(count)


        

l=[1,2,3]
sum=0
for i in range(len(l)):
    sum=sum*10+l[i]
sum=sum+1
result=[]
for i in str(sum):
    result.append(int(i))
print(result)
    
    