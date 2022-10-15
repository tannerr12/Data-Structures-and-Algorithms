class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        h = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heapq.heappush(h,matrix[r][c])
                
            
        
        val = 0
        while k != 0:
            k-=1
            val = heapq.heappop(h)
        
        
        return val
        