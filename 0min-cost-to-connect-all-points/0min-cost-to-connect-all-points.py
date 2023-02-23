class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        parent = [i for i in range(len(points))]
        rank = [1] * len(points)
        
        
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
        """

        arr = []
        
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
        
        adj = defaultdict(list)
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1,y1 = points[i]
                x2, y2 = points[j]
                man = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, man))
                adj[j].append((i, man))
        
        heap = []
        res = 0
        heappush(heap, (0, 0, 0))
        edges = len(points) -1
        for x,y in adj[0]:
            heappush(heap, (y, 0, x))
        
        
        
        while heap:
            
            weight, source, dest = heappop(heap)
            
            if union(source,dest):
                res += weight
                edges -=1
                if edges == 0:
                    break
            else:
                continue
            
            for x,y in adj[dest]:
                
                heappush(heap, (y, dest, x))
        
        return res
            
            
        