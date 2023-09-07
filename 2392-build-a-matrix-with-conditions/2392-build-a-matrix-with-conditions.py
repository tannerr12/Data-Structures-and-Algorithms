class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        #can we topo sort both the rows and the colums seperatly 
        
        #row -> 3 - > 1 -> 2
        #col -> 3 - > 2 -> 1
        
        # 0,0 -> 3 , 1,2 -> 1, 2, 1 - > 2
        
        #row -> 3  &  1
        #col -> 3  -> 1
        
        #0,0 -> 3, 0, 1 -> 1
        
        adjRow = defaultdict(set)
        adjCol = defaultdict(set)
        reqRow = defaultdict(set)
        reqCol = defaultdict(set)
        
        for x,y in rowConditions:
            adjRow[y].add(x)
            reqRow[x].add(y)
        
        for x,y in colConditions:
            adjCol[y].add(x)
            reqCol[x].add(y)
            
        
        posMp = defaultdict(int)
        
        #r,c = 0,0
        
        
        
        #print(adjRow)
        #print(adjCol)
        
        
        #3,0,0
        #0,0,0
        #0,0,0
        q = deque()
        for i in range(1,k+1):
            if i not in adjRow:
                q.append(i)
        
        
     
        rowOrder = []
        level = 0
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                rowOrder.append(node)
                
                for val in reqRow[node]:
                    adjRow[val].remove(node)
                    if len(adjRow[val]) == 0:
                        del adjRow[val]
                        q.append(val)
        
              
            level += 1
        
        
        
        for i in range(1,k+1):
            if i not in adjCol:
                q.append(i)
                
        
        level = 0
        
        colOrder = []
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                colOrder.append(node)
                
                for val in reqCol[node]:
                    adjCol[val].remove(node)
                    if len(adjCol[val]) == 0:
                        del adjCol[val]
                        q.append(val)
        
              
            level += 1
            
        if len(adjRow) > 0 or len(adjCol) > 0:
            return []
        
        #print(rowOrder)
        #print(colOrder)
        
        grid = [[0 for j in range(k)] for i in range(k)]
        
        
        for row, val in enumerate(rowOrder):
            col = colOrder.index(val)
            grid[row][col] = val
            
            
        return grid 
            