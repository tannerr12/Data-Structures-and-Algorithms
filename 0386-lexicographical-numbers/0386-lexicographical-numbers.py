class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        ans = []
        def dfs(cur):
            if cur > n:
                return 
            if cur > 0:
                ans.append(cur)
                
            
            
            for i in range(10):
                if i == 0 and cur == 0:
                    continue
                
                dfs(cur * 10 + i)
            
        
        dfs(0)
        
        return ans