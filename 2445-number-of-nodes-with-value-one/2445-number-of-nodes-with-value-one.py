class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        
        count = Counter(queries)
        
        #print(count)
        
        @cache
        def dfs(val,sign):
            
            if val > n:
                return 0
            
            if val in count and count[val] % 2:
                sign ^= 1
            left = dfs(val * 2, sign)
            right = dfs(val * 2 + 1, sign)
            
            return left + right + sign
        
        return dfs(1,0)