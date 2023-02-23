class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        parent = [i for i in range(len(points))]
        rank = [1] * len(points)
        
        """
        def find(val):
            
            if parent[val] == val:
                return val
            
            parent[val] = find(parent[val])
            
            return parent[val]
        
        def union(x,y):
           
            val1 = find(x)
            val2 = find(y)
            
            if val1 != val2:
                
                #they are not the same
                if rank[val1] > rank[val2]:
                    parent[val2] = val1
                elif rank[val2] > rank[val1]:
                    parent[val1] = val2
                
                else:
                    parent[val2] = val1
                    rank[val1] +=1
                
                return True
            return False
        

        arr = []
        #kruskals algorithm
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1,y1 = points[i]
                x2, y2 = points[j]
                man = abs(x1 - x2) + abs(y1 - y2)
                arr.append((man,i,j))
        
        
        arr.sort()
        res = 0
        #mst must have n-1 edges so we can exit early
        edges = len(points) -1
        for i,e in enumerate(arr):
            if edges == 0:
                break
            if union(arr[i][1], arr[i][2]):
                res += arr[i][0]
                edges -=1
        
        return res
        """
        #prims algoritm
        heap = []
        edges = len(points) -1
        visited = [False] * len(points)
        res = 0
        for i in range(1,len(points)):
           
            x1,y1 = points[i]
            x2, y2 = points[0]
            man = abs(x1 - x2) + abs(y1 - y2)
            heappush(heap, (man,i))
        
        visited[0] = True
        
        while heap and edges > 0:
            
            weight,dest = heappop(heap)
            
            if not visited[dest]:
                res += weight
                visited[dest] = True
                
                for j in range(len(points)):
                    if not visited[j]:
                        man = abs(points[j][0] - points[dest][0]) + abs(points[j][1] - points[dest][1])
                        heappush(heap,(man,j))
                    
                edges -=1
        
        return res
            
            
        