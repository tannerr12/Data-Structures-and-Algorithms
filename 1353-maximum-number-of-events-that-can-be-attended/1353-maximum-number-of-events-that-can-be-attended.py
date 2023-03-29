class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        
        #events.sort(key = lambda x: (x[1], x[0]))
        events.sort()
        #print(events)
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
                
            day += 1

        
        return res
                
            