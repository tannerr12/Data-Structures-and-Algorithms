class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        
        
        adj = defaultdict(set)
        leaf = []
        for x,y in trust:
            adj[x].add(y)
        
        
        for i in range(1,n+1):
            
            if i not in adj:
                leaf.append(i)
                
        
        
#print(leaf)
        if len(leaf) > 1:
            return -1
        
        for l in leaf:
            judge = True
            for i in range(1,n+1):
                
                if i == l:
                    continue
                    
                if l  not in adj[i]:
                    judge = False
                    break
                
            if judge:
                return l
        
        
        return -1
        