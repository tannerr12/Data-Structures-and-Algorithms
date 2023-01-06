class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        h = {}
        n = len(nums)
        count = 0
        total = 0
        for i in range(len(nums)):
            
            if nums[i]-i in h:
                count += h[nums[i]-i]
                h[nums[i]-i] +=1
            else:
                h[nums[i]-i] = 1
            
            total +=i
        
        return total - count