class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        
        #heap for meeting rooms time, meeting room number
        #going through each meeting we can try to allocate a meeting to a room
        #or if we cannot we can push the meeting onto a waiting heap which would cover [starttime, endtime/duration]
        score = defaultdict(int)
        mheap = []
        aheap = [i for i in range(n)]
        wdeq = deque()
        
        
        index = 0
        
        for i in range(10**6):
            while mheap and mheap[0][0] <= i:
                val, idx = heappop(mheap)
                heappush(aheap, idx)
                
            #handle all currently waiting rooms
            while wdeq and aheap:
                idx = heappop(aheap)
                s,e = wdeq.popleft()
                score[idx] += 1
                heappush(mheap, (i + (e - s), idx))
                
            
            if index < len(meetings) and aheap and meetings[index][0] <= i:
                idx = heappop(aheap)
                score[idx] += 1
                heappush(mheap, (meetings[index][1], idx))
                index += 1

            elif index < len(meetings) and meetings[index][0] <= i:
                wdeq.append((meetings[index][0], meetings[index][1]))
                index += 1
    
        
        
        #print(score)
        while wdeq:
            val,idx = heappop(mheap)
            s,e = wdeq.popleft()
            score[idx] += 1
            heappush(mheap, (val + (e - s), idx)) 
        
        
        mx = max(score.values())
        mn = float('inf')
        
        for x,y in score.items():
            if y == mx:
                mn = min(mn, x)
                
        
        return mn

                
                
            
        