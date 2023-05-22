class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            k = 1
        
        time = []
        mp = Counter(s)
        chars = []
        for key,val in mp.items():
            heappush(chars, [-val, key])
            
        res = []
        t = 0
        while chars or (time and time[0][0] == t):
            if time and time[0][0] == t:
                v1,v2,v3 = heappop(time)
                heappush(chars, [-v2,v3])
                
            total, char = heappop(chars)
            total = -total
            res.append(char)
            total -=1
            if total > 0:
                heappush(time, [t+k, total, char])
            
            t += 1
        
        
        if time:
            return ""
        else:
            return ''.join(res)
            
            
        