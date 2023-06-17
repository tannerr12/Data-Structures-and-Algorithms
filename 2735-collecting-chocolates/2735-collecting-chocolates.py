class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        res = sum(nums)
        mins = nums[:]
        
        #rotations
        for i in range(len(nums)):
            cost = i * x
            #numbers
            for j in range(len(nums)):
                    #grab the minimum value for this specific number
                mins[j] = min(mins[j], nums[(j+i) % len(nums)])
            res = min(res,sum(mins) + cost)
            
            
        
        return res
                
        