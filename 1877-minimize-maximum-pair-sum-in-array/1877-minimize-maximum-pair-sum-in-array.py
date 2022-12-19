class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        
        l,r = 0, len(nums) -1
        mx = 0
        while l < r:
            
            mx = max(mx, nums[l] + nums[r])
            
            l+=1
            r-=1
        
        
        return mx