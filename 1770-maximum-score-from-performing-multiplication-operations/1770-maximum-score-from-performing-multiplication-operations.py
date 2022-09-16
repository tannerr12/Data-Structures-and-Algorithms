class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int: 
        
        m = len(multipliers)
        n = len(nums)
        dp = collections.defaultdict(int)
        
        
        
        for r in range(m-1,-1,-1):
            for c in range(r,-1,-1):
                
                
                dp[(r,c)] = max(multipliers[r] * nums[c] + dp[(r+1,c+1)], multipliers[r] * nums[n-1 - (r-c)] + dp[(r+1,c)])
                
                
            
        
        
        return dp[(0,0)]