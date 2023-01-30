from sortedcontainers import SortedList

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        events = defaultdict(list)
        
        sl = SortedList()
        for rx,ry in rectangles:
            events[rx].append((0,ry,-1))
            
        
        for index, (px,py) in enumerate(points):
            events[px].append((1,py,index))
        
        
        N = len(points)
        ans = [None] * N
        
        for key in sorted(events.keys(), reverse=True):
            events[key].sort()
            
            for e,y,t in events[key]:
                if e == 1:
                    count = len(sl) - sl.bisect_left(y)
                    ans[t] = count
                else:
                    sl.add(y)
        
        return ans
        
        
                
        