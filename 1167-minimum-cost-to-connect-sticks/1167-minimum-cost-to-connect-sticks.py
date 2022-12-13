class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        if len(sticks) ==1:
            return 0
        
        res = 0
        heapq.heapify(sticks)
        
        while sticks and len(sticks) > 1:
            s2 =0 
            s1 = heappop(sticks)
            if sticks:
                s2 = heappop(sticks)
            
            res += s1 + s2
            
            heapq.heappush(sticks, s1+s2)
    
        
        return res
            