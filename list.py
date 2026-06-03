# l=[10,20,30,40,50,60]
# l.sort()
# print(l)
# l.append(20)
# l.extend("hi")
# l.insert(1,"hello")
# print(l)
# print(l.index(10))
# print(l)
# print(l.count(10))
# (print(l))
# l.reverse()
# print(l)
# l.pop()
# print(l)
# print(l.pop())
# print(l)
# print(l.pop(1))
# print(l)
# l.remove(20)
# print(l)
# l.copy()
# print(l)
# l.clear()
# print(l)


# l=[10,20,30,40,50]
# sum1=0
# for i in range(len(l)):
#     sum1+=l[i]
# print("sum:", sum1)

# l=[10,20,30,40,50]
# product=1
# for i in range(len(l)):
#     product*=l[i]
# print("product:", product)

# l=[10,20,30,40,50]
# max1=0
# for i in range(len(l)):
#     if max1<l[i]:
#         max1=l[i]
# print("max:", max1)

# l=[10,20,30,40,50]
# min1=l[0]
# for i in range(len(l)):
#     if min1>l[i]:
#         min1=l[i]
# print("min:", min1)

# l=[10,20,30,40,50]
# count=0
# for i in l:
#     count+=1
# print("length:", count)


l=[4,3,2,1]
sum=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        l.index(l[i])
        sum+=1
        print(l)