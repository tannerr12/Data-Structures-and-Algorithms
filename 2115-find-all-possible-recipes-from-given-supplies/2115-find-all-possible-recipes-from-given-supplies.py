class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        adj = defaultdict(int)
        indegree = defaultdict(set)
        for i in range(len(recipes)):
            
            for j in range(len(ingredients[i])):
                adj[recipes[i]] += 1
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
                    
                    adj[val] -=1
                    
                    if adj[val] == 0:
                        res.append(val)
                        q.append(val)
        
        return res