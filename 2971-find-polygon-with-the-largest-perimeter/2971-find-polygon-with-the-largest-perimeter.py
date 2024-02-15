class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        
        nums.sort()
        l,r = 0, len(nums) -1
        
        prefix = [0]
        
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        def isGood(mid):
            return nums[mid] < prefix[mid]
        
        res = -1
        for i in range(2,len(nums)):
            if isGood(i):
                res = i
                
        
        if res == -1:
            return -1
        return prefix[res+1]
        