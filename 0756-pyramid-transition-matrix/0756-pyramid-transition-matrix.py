class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        
        adj = defaultdict(list)
        
        for word in allowed:
            adj[word[0] + word[1]].append(word[2])
            
        @cache
        def dfs(i,last,prev):
            
            if len(prev) == 1:
                return True
            res = False
       
                
            block = prev[i-1] + prev[i]

            if block not in adj:
                return False

            for val in adj[block]:

                if (len(last + val) < len(prev) -1):
                    res = res or dfs(i + 1, last + val, prev)
                else:
                    res = res or dfs(1,'', last + val)
                
            return res
        
        return dfs(1,'', bottom)