class Solution:
    def areSentencesSimilarTwo(self, s1: List[str], s2: List[str], sp: List[List[str]]) -> bool:
        if len(s1) != len(s2):
            return False
        parent= {}
        rank = defaultdict(int)
        
        def find(val):
            
            if parent[val] == val:
                return val
            
            parent[val] = find(parent[val])
            return parent[val]
            
        def union(x,y):
            
            v1,v2 = find(x), find(y)
            
            
            if v1 != v2:
                
                if rank[v1] > rank[v2]:
                    parent[v2] = v1
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                    
                else:
                    parent[v2] = v1
                    rank[v1] += 1
                
                
        
        def isConnected(x,y):
            return find(x) == find(y)
        
        
        for x,y in sp:
            if x not in parent:
                parent[x] = x
            if y not in parent:
                parent[y] = y
            union(x,y)

        for w1,w2 in zip(s1,s2):
            if w1 == w2:
                continue
            if w1 not in parent or w2 not in parent or not isConnected(w1,w2):
                return False
        
        return True
            
            
            
        