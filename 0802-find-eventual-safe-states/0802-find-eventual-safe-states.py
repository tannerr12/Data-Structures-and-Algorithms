class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:


        terminal = set()
        for i in range(len(graph)):
            g = graph[i]
            if len(g) == 0:
                terminal.add(i)

        
        seen = {}
        loopCheck = set()
        def dfs(i):

            if i in seen:
                return seen[i]
            elif i in loopCheck:
                return 
            
            if len(graph[i]) == 0:
                b = i in terminal
                seen[i] = b
                return b
            loopCheck.add(i)
            m= True  
            for x in graph[i]:
                m = m and dfs(x)

            seen[i] = m
            return m

        
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
            loopCheck = set()
        return res
            
