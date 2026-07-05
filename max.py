# l = [10, 20, 30, 40, 50]
# max1=max(l)
# l.remove(max1)
# max2=max(l)
# l.remove(max2)
# max3=max(l)
# print("3rd max value:", max3)

# l=[10,20,70,40,50]
# max1=0
# max2=0
# max3=0
# for i in l:
#     if i>max1:
#         max3=max2
#         max2=max1
#         max1=i
#     elif i>max2:
#         max3=max2
#         max2=i
#     elif i>max3:
#         max3 = i
# print("3rd max value:", max3)

# l=[1,2,3,4,5]
# max=0
# l2=[max:= val for val in l if max<val]
# print(max)


l=[1,2,3,4,5]
min=l[0]
l2=[min:= val for val in l if min>val]
print(min)