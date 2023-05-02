class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        if 0 in nums:
            return 0
        neg = 0
        for val in nums:
            if val < 0:
                neg +=1
                
        
        if neg % 2:
            return -1
        else:
            return 1