# nums =[2,2,1,1,1,2,2]
# d={}
# for i in nums:
#     d[i]=d.get(i,0)+1
# for j in d:
#     if d[j]>len(nums)//2:
#         print(j)
#         break
    
# t=(1,2,3,1,2,3,4,3,)
# d={}
# for i in t:
#     d[(i)]=d.get(i,0)+1
# print(d)
    
    
arr=[1,2,2,1,1,3]
d={}
l=(len(arr))
for i in arr:
    d[i]=d.get(i,0)+1
    if i==d:
       print(True)
    if(i==d):
        print(False)
        