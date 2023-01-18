class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def scan(arr):
            
            dp = [1] * len(arr)
            for i in range(1, len(arr)):
                for j in range(i):
                    if arr[i] > arr[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            
            
        
            return dp
        

                    
        left = scan(nums)
        right = scan(nums[::-1])
                
        
        res = 0
        n = len(nums)
        for i in range(1,len(nums)-1):
            
            if left[i] > 1 and right[n-i-1] > 1:
                res = max(res,left[i] + right[n-i-1]-1)
        
        
        return n - res