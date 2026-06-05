# l=[10,20,30,40,50,60,70]
# print(l[0:5:2]) #step+ve,index+ve-- [start,end,step]
# print(l[:5:1])#step+ve, index+ve---[end,step]
# print(l[::1])#step+ve,index-+ve---[step]
# print(l[-5:-1:2])#step+ve,index-ve--[start,end,step]
# print(l[:-1:1])#step+ve,index-ve--[end,step]
# print(l[-1:])#step+ve,index-ve--[start]
# print(l[-0:-5:-1])#step-ve,index-ve--[start,end,step]
# print(l[-5::-1])#step-ve,index-ve--[start,step]
# print(l[::-1])#step-ve,index-ve--[step]
# print(l[5:5:-1])#step-ve, index+ve--[start,end,step]
# print(l[5::-1])#step-ve, index+ve--[start,step]
# print(l[:4:-1])#step-ve, index+ve--[end,step]

# sum=l[0]+l[1]
# print(sum)
# result=((l.index(2),l.index(7)))
# print(result)
# print(l.index(2))
# print(l.index(7))

# for i in str(sum):
#     result.append(int(i))
# print(result)
# l=[2,7,11,5]
# for i in range(1):
#     for j in range(i+1,4):
#         if l[i]+l[j]==9:
#             print([i,j])
            
nums=[4,5,6,7,0,1,2] 
target=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(nums.index(4))