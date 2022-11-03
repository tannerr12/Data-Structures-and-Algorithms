class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        h = defaultdict(int)
        
        
        
        for r in range(len(mat)):
            
            for c in range(len(mat[r])):
                
                h[mat[r][c]] +=1
                
        
        
        
        heap = []
        
        for key,val in h.items():
            if val == len(mat):
                
                heapq.heappush(heap,key)
                
                
        
        
        
        return heapq.heappop(heap) if len(heap) > 0 else -1