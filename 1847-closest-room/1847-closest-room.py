from sortedcontainers import SortedList
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        

        ids = []
        rooms.sort(key=lambda x : (x[1], x[0]))
        for i in range(len(rooms)):
            ids.append(rooms[i][0])
            
        ids.sort()
        quer = []
        
    
        for i,(x,y) in enumerate(queries):
            quer.append((i, x, y))
            
        
        quer.sort(key=lambda x: (x[2], x[1]))
        
        
        print(quer)
        print(rooms)
        ans = [-1] * len(queries)
        idx = 0
        
        #mp = set([x for x in ids])
        SL = SortedList([x for x in ids])
        #print(mp)
        for i,x,y in quer:
            
            while idx < len(rooms) and rooms[idx][1] < y:
                SL.remove(rooms[idx][0])
                idx +=1
                
            if idx >= len(rooms):
                break
            
            pos = bisect_left(SL, x)
            pos -= 1
            if pos >= len(SL) -1:
                ans[i] = SL[-1]
            else:

                if abs(SL[pos+1] - x) < abs(SL[pos] - x):
                    ans[i] = SL[pos+1]
                    
                else:
                    ans[i] = SL[pos]
                   
            
        
        return ans