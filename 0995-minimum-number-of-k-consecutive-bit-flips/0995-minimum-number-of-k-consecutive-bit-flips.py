class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        
        res = 0
        seenI = [0] * len(nums)
        curr = 0
        
        for i in range(len(nums)):
        
            if i - k >=0:
                
                if seenI[i-k] > 0:
                    curr -= 1
            
            if curr % 2 == nums[i]:
                
                if i+k > len(nums):
                    return -1
                
                seenI[i] =1
                curr +=1
                res +=1
        
        
        return res
