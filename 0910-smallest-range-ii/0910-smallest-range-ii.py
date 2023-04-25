class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
                
        nums.sort()
        res = nums[-1] - nums[0]
        
        for i in range(len(nums)-1):
            #compare 2 elements at a time
            
            j = i + 1
            
            #adding to the lower number and subtracting from the higher number
            #this will simulate the lowest number we will see
            low = min(nums[0] + k, nums[j] - k)
            #max number seen so far
            high = max(nums[len(nums)-1]-k, nums[i]+k)
            
            res = min(res, high - low)
            
        
        return res
