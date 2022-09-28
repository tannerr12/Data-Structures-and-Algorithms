class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = [i for i in range(26)]
        
        

        def union(a,b):
            
            a = find(a)
            b = find(b)
                    
            parent[b] = a
            
        
        def find(a):
            
            while a != parent[a]:
                a = parent[a]
            
            
            return a
        
            
        
        for i in range(len(equations)):
            
            eq = equations[i]
            
            symbol = eq[1]
            a,b = eq[0],eq[3]
            
            aVal = ord(a) - ord('a')
            bVal = ord(b) - ord('a')
            
            if symbol == '=':
                
                union(aVal,bVal)
        
        
        for i in range(len(equations)):
            
            eq = equations[i]
            
            symbol = eq[1]
            a,b = eq[0],eq[3]
            aVal = ord(a) - ord('a')
            bVal = ord(b) - ord('a')
            
            if symbol == '!':
                
                if find(aVal) == find(bVal):
                    return False
        
        
        return True
        
        
            
                               
            
            
            
            