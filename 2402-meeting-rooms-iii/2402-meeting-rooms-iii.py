class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        
        #heap for meeting rooms time, meeting room number
        #going through each meeting we can try to allocate a meeting to a room
        #or if we cannot we can push the meeting onto a waiting heap which would cover [starttime, endtime/duration]
        score = defaultdict(int)
        mheap = []
        aheap = [i for i in range(n)]
        
        
        for x,y in meetings:
            while mheap and mheap[0][0] <= x:
                val, idx = heappop(mheap)
                heappush(aheap, idx)
                
            if aheap:
                idx = heappop(aheap)
                heappush(mheap, (y, idx))
            
            else:
                rt, idx = heappop(mheap)
                heappush(mheap, (rt + y - x, idx))
            
            score[idx]+= 1
            
        mx = max(score.values())
        mn = float('inf')
        
        for x,y in score.items():
            if y == mx:
                mn = min(mn, x)
                
        
        return mn

   