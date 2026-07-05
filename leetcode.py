from git import List


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

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            for digit in str(num):
                result.append(int(digit))
        return result
        
        
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        l = 0
        for i, digit in enumerate(s):
            if i % 2 == 0:
                l+=int(digit)
            else:
                l -= int(digit)
        return l
