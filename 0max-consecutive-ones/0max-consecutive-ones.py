class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for num in nums:
            
            if num == 0:
                count = 0
            else:
                count +=1
            
            
            res = max(res,count)
        
        return res