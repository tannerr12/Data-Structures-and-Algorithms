class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = defaultdict(list)
        self.n = n
        
        for x,y,w in edges:
            self.adj[x].append([w,y])
        
       

    def addEdge(self, edge: List[int]) -> None:
        x,y,w = edge
        self.adj[x].append([w,y])
        

    def shortestPath(self, node1: int, node2: int) -> int:
        
        heap = []
        heappush(heap, [0,node1])
        seen = set()
        while heap:
            
            w,node = heappop(heap)
            if node == node2:
                return w
            seen.add(node)
            for weight,n in self.adj[node]:
                if n in seen:
                    continue
                heappush(heap, [w + weight,n])
        
        
        
        return -1
                
            
                
                
            


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)