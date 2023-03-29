class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        
        #
        events.sort()
        res = 0
        day = events[0][0]
        i = 0
        heap = []
        while i < len(events) or heap:
            
            
            
            while i < len(events) and events[i][0] <= day:
                
                heappush(heap, events[i][1])
                i+=1
                
            while heap and heap[0] < day:
                heappop(heap)
            
            
            if heap:
                heappop(heap)
                res +=1
            
            elif not heap and i < len(events):
                
                day = events[i][0]
                continue
            day += 1

        
        return res
                
            