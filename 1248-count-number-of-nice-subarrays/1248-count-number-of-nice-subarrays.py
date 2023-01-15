class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        idxMap = {}
        prevOdd = len(nums)
        for i in range(len(nums) -1,-1,-1):
            if nums[i] % 2:
                idxMap[i] = prevOdd
                prevOdd = i
        
    
        l = 0
        
        odds = 0
        res = 0
        for i in range(len(nums)):
            
            if nums[i] % 2:
                odds+=1
                
            
            while odds >= k:
                
                if nums[l] % 2:
                    odds -=1
                    
                l+=1    
                res += 1 + (idxMap[i] - (i + 1))
        
        return res
            
            