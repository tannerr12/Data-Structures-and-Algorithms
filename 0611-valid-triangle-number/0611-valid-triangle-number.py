class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        res = 0
        
        k = 0
        for i in range(len(nums)):
            k = i + 2
            for j in range(i+1, len(nums)):
                
                a = nums[i]
                b = nums[j]
                target = a + b - 1
                
            
                while k < len(nums) and nums[k] <= target:
                    k += 1
    
                res += max(0,k - 1 - j)
                
        
        return res
                
                