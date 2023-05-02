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
        if hour > mn:
            count = 0
            thour = hour
            while int(thour) != int(mn):
                thour += 1
                count +=1
                thour %=12

            if thour <= mn:
                res = min(res, (count + abs(thour - mn)) * anglephour)
            else:
                res = min(res, (abs(count - abs(thour - mn))) * anglephour) 
        else:
            count = 0
            tmin = mn
            while int(tmin) != int(hour):
                tmin += 1
                count +=1
                tmin %=12

            if tmin <= hour:
                res = min(res,abs((count + abs(hour - tmin)) * anglephour))
            else:
                res = min(res, abs((abs(count - abs(hour - tmin))) * anglephour))
        return res