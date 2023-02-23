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
        

        arr = []
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1,y1 = points[i]
                x2, y2 = points[j]
                man = abs(x1 - x2) + abs(y1 - y2)
                arr.append((man,i,j))
        
        
        arr.sort()
        res = 0
        for i,e in enumerate(arr):
            if union(arr[i][1], arr[i][2]):
                res += arr[i][0]
        
        
        return res
            