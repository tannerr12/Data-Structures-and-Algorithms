class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        l,r = 0,0

        res = 0
        while r < len(nums) -1:
            furthest = 0
            for i in range(l,r + 1):
                furthest = max(furthest, i + nums[i])
            
            l= r+1
            r = furthest
            res +=1
            
        
        
        return res