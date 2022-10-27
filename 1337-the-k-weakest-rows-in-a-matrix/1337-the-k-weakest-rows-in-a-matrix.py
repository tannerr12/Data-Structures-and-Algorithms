class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        
        
        
        for i in range(len(mat)):
            
            l,r = 0,len(mat[i])- 1
            
            if mat[i][0] ==0:
                heapq.heappush(heap, (0,i))
                
                continue
            if mat[i][-1] == 1:
                heapq.heappush(heap, (len(mat[i]), i))
                continue
            while l <= r:
                
                
                curr = (l+r) //2 
                
                
                if mat[i][curr] == 0 and mat[i][curr -1] == 1:
                    
                    heapq.heappush(heap, (curr,i))
                    break
                    
                elif mat[i][curr] == 0:
                    r = curr -1 
                    
                else:
                    
                    l = curr +1
        
        
        
        
        res = []
        
        while k > 0:
            
            res.append(heapq.heappop(heap)[1])
            k-=1
        return res
            
                    