class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        heap = []
        
        for s,e in intervals:
            
            if len(heap) == 0 or heap[0] >= s:
                heappush(heap, e)
            elif heap[0] < s:
                heappop(heap)
                heappush(heap, e)
            
            
        
        return len(heap)
            
            
        
        