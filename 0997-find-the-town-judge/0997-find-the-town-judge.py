class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        
        
        adj = defaultdict(set)
        leaf = -1
        for x,y in trust:
            adj[x].add(y)
        
        
        for i in range(1,n+1):
            
            if i not in adj:
                if leaf != -1:
                    return -1
                
                leaf = i
                
                
    
        
        judge = True
        for i in range(1,n+1):
                
            if i == leaf:
                continue
                    
            if leaf not in adj[i]:
                judge = False
                break
                
        
        
        return -1 if not judge else leaf
        