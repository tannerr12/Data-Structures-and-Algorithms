class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = [i for i in range(len(strs))]
        rank = [0] * len(strs)
        count = len(strs)
        def find(val):
            
            if val == parent[val]:
                return val
            
            parent[val] = find(parent[val])
            
            return parent[val]
        
        
        def union(x,y):
            nonlocal count
            v1,v2 = find(x),find(y)
            
            
            if v1 != v2:
                
                
                if rank[v1] > rank[v2]:
                    
                    parent[v2] = v1
                    
                elif rank[v2] > rank[v1]:
                    
                    parent[v1] = v2
                
                else:
                    
                    parent[v2] = v1
                    rank[v1] +=1
                
                
                count -=1
                return False
            
            return True
        
        
        def isConnected(x,y):
            
            return find(x) == find(y)
        
        for i in range(len(strs)):


            for j in range(i+1, len(strs)):
                
                if isConnected(i,j):
                    continue
                if strs[i] == strs[j]:
                    union(i,j)
                    continue
                char1 =[]
                char2 =[]
                for k in range(len(strs[i])):
                    c1,c2 = strs[i][k],strs[j][k]
                    if c1 != c2:
                        char1.append(c1)
                        char2.append(c2)
                
                
                if len(char1) == 2 and char1[-1] == char2[0] and char1[0] == char2[-1]:
                    union(i,j)
        
        
        
        return count
                