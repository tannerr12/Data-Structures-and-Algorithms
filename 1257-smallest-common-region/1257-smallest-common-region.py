class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        adj = defaultdict(list)

        for i in range(len(regions)):
            
            for j in range(1,len(regions[i])):
                adj[regions[i][0]].append(regions[i][j])

                    
       
        res = None
        
       
        def dfs(node):
            nonlocal res
            
            r1, r2 = False, False
            
            if node == region1:
                r1 = True
            if node == region2:
                r2 = True
                
            for val in adj[node]:
                
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
        
            
        
        
        
        