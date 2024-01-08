class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        adj = {}

        for i in range(len(regions)):
            adj[regions[i][0]] = i
                    
       
        res = None
        
       
        def dfs(node):
            nonlocal res
            
            r1, r2 = False, False
            
            if node == region1:
                r1 = True
            if node == region2:
                r2 = True
            if node in adj:
                for i in range(1,len(regions[adj[node]])):
                    val = regions[adj[node]][i]
                    v1,v2 = dfs(val)

                    r1 = r1 or v1
                    r2 = r2 or v2

                    if not res and r1 and r2:
                        res = node
                        return [True,True]


                
            return [r1,r2]
            
        
        
        for val in regions:
            dfs(val[0])
            if res:
                return res
        
            
        
        
        
        