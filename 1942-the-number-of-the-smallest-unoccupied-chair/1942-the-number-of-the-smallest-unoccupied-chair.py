class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        #add the index to our list so we can sort
        for i in range(len(times)):
            times[i].append(i)
            
        times.sort(key = lambda x:(x[0], x[1]))
        
        
        heapLeave = []
        heapOpen = []
        count = 0
        
        i = 0
        #trick to save on space is to only store rearrivals in heapOpen since they will always be less than or equal to our count so if we
        #have anything in heapOpen we can pop that first, than if we have nothing in heapOpen we can use the counter which means all the chairs behind us
        #are filled and we must start using new chairs
        while i <= len(times):
            
            arr,leav,idx = times[i]
            
            while heapLeave and heapLeave[0][0] <= arr:
                #time leave, his chair
                l,c = heappop(heapLeave)
                #we only need his chair
                heappush(heapOpen, c)
            
            if heapOpen:
                #old chair being reused
                chair = heappop(heapOpen)
            else:
                #new chair
                chair = count
                count +=1
            #break early we found our friend
            if idx == targetFriend:
                return chair
            
            #someone sat down, we must add their leave time
            heappush(heapLeave, (leav, chair))
            
            i+=1
        
        
                
            