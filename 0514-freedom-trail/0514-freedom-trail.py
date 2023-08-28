class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        mp = defaultdict(list)
        for i in range(len(ring)):
            #find min cost to get char to 0
            mp[ring[i]].append(i)
            
        #print(mp)
        heap = []
        heappush(heap, (0, 0, 0))
        seen = set()
        while heap:
            
            for i in range(len(heap)):
                
                cost, pos, keypos = heappop(heap)
                
                if (pos,keypos) in seen:
                    continue
                    
                seen.add((pos,keypos))
                
                if keypos == len(key):
                    return cost
                
                for p in mp[key[keypos]]:
                    
                    heappush(heap, (cost + 1 + min(abs(pos - p),abs(p - len(ring))  + pos, abs(pos - len(ring)) + p), p, keypos +1))
                
                