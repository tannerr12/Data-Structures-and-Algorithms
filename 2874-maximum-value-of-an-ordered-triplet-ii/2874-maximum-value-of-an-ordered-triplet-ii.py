class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        largest = [0] * len(nums)
        
        for i in range(len(nums)-2,-1,-1):
        
            largest[i] = max(largest[i+1], nums[i+1])
        
        
        #print(largest)
        
        largestLeft = [0] * len(nums)
        
        for i in range(1, len(nums)):
        
            largestLeft[i] = max(largestLeft[i-1], nums[i-1])
        
        #print(largestLeft)
        res = 0
        for i in range(len(nums)):
            res = max(res,(largestLeft[i] - nums[i]) * largest[i])
        
        
        return res