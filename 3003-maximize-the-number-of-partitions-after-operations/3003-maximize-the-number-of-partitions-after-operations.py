class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        
        #k = 26 means the answer is always 1
        #the initial partitions are fixed
        
        c = Counter(s)
        if k > len(c) or k == 26:
            return 1

        
        #10,000 * 2 * 26 
        @cache
        def dfs(i,used,mask):
            
            if i == len(s):
                return 1
            
            total = mask.bit_count()
            cur = ord(s[i]) - ord('a')
            res = 0
            if not used:
                for j in range(26):
                    if mask & (1 << j) == 0 and j != cur:
                        res = max(res, dfs(i+1, 1, (0 if total == k else mask) | (1 << j)) + (total == k))
        
            
            

            if total == k and mask & (1 << cur) == 0:
                res = max(res, dfs(i+1, used, 0 | (1 << cur)) + 1)
            else:
                res = max(res, dfs(i+1, used, mask | (1 << cur)))    
            
            return res
        
        
        return dfs(0,0,0)