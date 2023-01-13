class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        
        
        res = 0
        adj = defaultdict(set)
        
        
        for i, [x,y] in enumerate(edges):
            if x == -1:
                continue
            adj[x].add((i, y))
            
        
        @cache
        def getMaxNotChoosing(node):
            total = 0
            for v,w in adj[node]:
                total += getMaxChoosing(v)
            
            
            return total
        @cache
        def getMaxChoosing(node):
            
            
            edgeCount = 0
            for v,w in adj[node]:
                edgeCount += getMaxChoosing(v)
            
            best = edgeCount
            
            for v,w in adj[node]:
                best = max(best, edgeCount - getMaxChoosing(v) + getMaxNotChoosing(v) + w)
                
            
            
            return best
            
        return getMaxChoosing(0)