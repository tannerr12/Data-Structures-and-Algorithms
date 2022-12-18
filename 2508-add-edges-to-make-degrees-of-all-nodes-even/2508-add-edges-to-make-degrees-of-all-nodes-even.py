class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        
        for x,y in edges:
            adj[x-1].append(y-1)
            adj[y-1].append(x-1)
            
        odd = []
        vals = []
        #print(adj)
        for key,val in adj.items():
            
            if len(val) % 2 == 1:
                odd.append(key)
                
                
   
        
        if len(odd) == 0:
            return True
        
        if len(odd) % 2 or len(odd) > 4:
            return False
        
        if len(odd) == 2:
            
            
            for i in range(n):
                
                if i != odd[0] and i != odd[1] and odd[0] not in adj[i] and odd[1] not in adj[i]:
                    return True
            
            
            if odd[0] in adj[odd[1]]:
                return False
            return True
        
        
        def checkIn(e,v):
            if e in adj[v]:
                return False
            return True
            
        if len(odd) == 4:
            
            if checkIn(odd[0], odd[1]) and checkIn(odd[2], odd[3]):
                return True
            if checkIn(odd[0], odd[2]) and checkIn(odd[1], odd[3]):
                return True
            if checkIn(odd[0], odd[3]) and checkIn(odd[1], odd[2]):
                return True
            
            return False
            
            
            