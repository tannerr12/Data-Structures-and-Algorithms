class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        memo = {}
        res = []
        def dfs(i,temp):
            nonlocal res
            if i in memo:
                return memo[i]
            
            
            temp.append(i)
            for j in range(len(graph[i])):
                val = graph[i][j]
               
                dfs(val,temp)
            
            
            if len(graph) -1 == i:
               # temp.append(i)
                res.append(temp.copy())
            
        
            temp.pop()
            return 1
            

        dfs(0,[])
        return res
        