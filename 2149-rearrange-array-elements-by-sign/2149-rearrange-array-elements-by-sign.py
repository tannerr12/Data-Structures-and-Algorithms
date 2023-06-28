class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p,n = 0,0
        idx = 0
        ans = []
        while p < len(nums) or n < len(nums):
                    
            while p < len(nums) and nums[p] < 0:
                p+=1
            
            while n < len(nums) and nums[n] >= 0:
                n+=1
            
            if p < len(nums):
                ans.append(nums[p])
                p+=1
            if n < len(nums):
                ans.append(nums[n])
                n+=1

        return ans
            
                
            
        
        