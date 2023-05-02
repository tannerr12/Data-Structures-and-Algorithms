class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #full circle is 360
        #convert both to 12
        
        
        #convert minute to 12
        anglephour = 360 // 12
        conv = 60 // 12
        
        mn = minutes / conv
        
        hour += mn / 12
        
        hour %= 12
        #print(hour)
        #print(mn)
        
        res = abs(hour - mn) * anglephour  
        res = min(res, 360 - res)
        return res