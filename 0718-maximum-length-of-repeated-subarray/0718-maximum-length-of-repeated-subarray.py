class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1), len(nums2)
        
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        res = 0
        for i in range(1, len(dp)):
            
            for j in range(1, len(dp[0])):
                
                if nums1[j-1] == nums2[i-1]:
                    
                    dp[i][j] = 1 + dp[i-1][j-1]
                    
                    res = max(res,dp[i][j])
                    
        
        
        return res