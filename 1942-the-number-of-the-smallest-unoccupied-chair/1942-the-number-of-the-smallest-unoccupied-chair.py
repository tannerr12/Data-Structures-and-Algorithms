class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        for i in range(len(times)):
            times[i].append(i)
            
        times.sort(key = lambda x:(x[0], x[1]))
        
        #print(times)
        
        
        #hour = 0
        #heapArrive = []
        heapLeave = []
        
        av = []
        count = 0
        
        i = 0
        
        while i <= len(times):
            arr,leav,idx = times[i]
            
            
            while heapLeave and heapLeave[0][0] <= arr:
                
                l,c = heappop(heapLeave)
                heappush(av, c)
            
            if av:
                chair = heappop(av)
            else:
                chair = count
                count +=1
            if idx == targetFriend:
                return chair
            
            heappush(heapLeave, (leav, chair))
            
            i+=1
        
        
                
            