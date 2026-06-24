class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        return(num-1)%9+1

digits = [1,2,3]

for i in range(len(digits)):
    sum=sum*10+digits[i]
    sum=sum+1
    result=[]
for i in str(sum):
    result.append(int(i))
print(result)
