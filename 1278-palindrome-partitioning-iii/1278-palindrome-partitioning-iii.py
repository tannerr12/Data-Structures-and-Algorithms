class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        @cache
        def minCostPal(i, st):
            
            if i == len(st) // 2:
                return 0
            res = float('inf')
            #they are the same
            if st[i] == st[-i-1]:
                res = min(res, minCostPal(i+1, st))
            
            else:
                #change left or right
                res = min(res, minCostPal(i+1, st) + 1)
            
            
            return res
        
        @cache
        def dfs(i, last, count):

            if i >= len(s):
                return float('inf')
            if count == k-1:
                return minCostPal(0, s[last+1:])

            
            res = float('inf')
     
            #split
            res = min(res, dfs(i+1, i, count +1) + minCostPal(0, s[last+1:i+1]))
            
            
            #dont split
            res = min(res, dfs(i+1, last, count))
            
            return res
        
        return dfs(0,-1, 0)