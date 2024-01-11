class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        
        graph = defaultdict(list)
        tickets.sort(key = lambda x:(x[1]),reverse=True)
        for x,y in tickets:
            graph[x].append(y)
        
        ans = []
        def dfs(node):
            
            while graph[node]:
                dfs(graph[node].pop())
            
            ans.append(node)
        
        
        dfs('JFK')
        
        ans.reverse()
        return ans
        
        

            
            