class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        adj = defaultdict(set)
        indegree = defaultdict(set)
        for i in range(len(recipes)):
            
            for j in range(len(ingredients[i])):
                adj[recipes[i]].add(ingredients[i][j])
                indegree[ingredients[i][j]].add(recipes[i])
        
        #print(adj)
        q = deque()
        
        for val in supplies:    
            q.append(val)
            
        res = []
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                for val in indegree[node]:
                    
                    adj[val].remove(node)
                    
                    if len(adj[val]) == 0:
                        res.append(val)
                        q.append(val)
        
        return res