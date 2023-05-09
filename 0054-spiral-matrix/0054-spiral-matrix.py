class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        n = len(matrix) -1
        m = len(matrix[0]) -1
        total = len(matrix) * len(matrix[0])
        res = []
        visit = set()
        layer =0
        while total > 0:
            
            #left to right
            for i in range(len(matrix[0])):
                if (layer,i) in visit:
                    continue
                visit.add((layer,i))
                res.append(matrix[layer][i])
                total -=1
            
       
            
            #right down
            for i in range(len(matrix)):
                if (i,m - layer) in visit:
                    continue
                visit.add((i,m - layer))
                res.append(matrix[i][m - layer])
                total -=1
            
  
            #right left
            for i in range(len(matrix[0])-1,-1,-1):
                if (n - layer,i) in visit:
                    continue
                visit.add((n - layer,i))
                res.append(matrix[n - layer][i])
                total -=1
            
        
            #bottom up
            for i in range(len(matrix) -1,-1,-1):
                if (i,layer) in visit:
                    continue
                visit.add((i,layer))
                res.append(matrix[i][layer])
                total -=1
      
            layer +=1
            
        return res