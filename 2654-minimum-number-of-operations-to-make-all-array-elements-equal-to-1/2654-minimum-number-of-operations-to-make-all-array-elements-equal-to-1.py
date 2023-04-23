class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones > 0:
            return len(nums) - ones
        
        res = float('inf')
        for i in range(len(nums)):
            current = nums[i]
            for j in range(i,len(nums)):
                current = gcd(nums[j],current)
                
                if current == 1:
                    res = min(res,j - i + len(nums) -1)
                    break
        
        
        return res if res != float('inf') else -1
                    
                
            
            
            