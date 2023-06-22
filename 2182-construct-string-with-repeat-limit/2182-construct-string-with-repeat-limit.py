class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        c = Counter(s)
        heap = []
        for key,val in c.items():
            heappush(heap, (-ord(key), val))
            
        res = []
        repeat = 0
        repVal = ''
        while heap:
            
            val,count = heappop(heap)
            val = chr(-val)
            if val == repVal and repeat == repeatLimit and heap:
                v2,c2 = heappop(heap)
                v2 = chr(-v2)
                res.append(v2)
                repeat = 0
                if c2-1 > 0:
                    heappush(heap, (-ord(v2),c2-1))
            
            if repeat < repeatLimit or val != repVal:
                res.append(val)
            if count -1 > 0:
                heappush(heap,(-ord(val), count-1))
            if repVal == val:
                
                repeat += 1
            else:
                repVal = val
                repeat = 1
 
        return ''.join(res)
            