class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = {}

        def dfs(i):
            
            if i in memo:
                return memo[i]
            
            res = 1
            for j in range(i+1, min(i+d+1, len(arr))):
                if arr[j] >= arr[i]:
                    break
                
                res = max(res, dfs(j) + 1)
            
            for j in range(i-1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                
                res = max(res, dfs(j) + 1)
            
            memo[i] = res
            return res
        
        ans = 1
        for i in range(len(arr)):
            ans = max(ans, dfs(i))
            
        return ans