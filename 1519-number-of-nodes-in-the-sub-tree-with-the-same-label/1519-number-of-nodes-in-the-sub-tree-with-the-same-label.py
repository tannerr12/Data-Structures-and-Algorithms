class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        
        adj= defaultdict(list)
        
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)


        res = [0] * n
        
        
        def dfs(node,parent):

    
            total = 0
            letter = [0] * 26
            for child in adj[node]:
                if child == parent:
                    continue
                
                f = dfs(child,node)
                
                for i in range(26):
                    letter[i] += f[i]
                 
                
            
            letter[ord(labels[node]) - ord('a')] +=1
            res[node] = letter[ord(labels[node]) - ord('a')]
            return letter
                
        
    
        dfs(0,-1)
            
        
        #print(res)
        return res
            