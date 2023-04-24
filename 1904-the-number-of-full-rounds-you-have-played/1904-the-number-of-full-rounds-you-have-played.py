class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        
        
        start = loginTime.split(':')
        end = logoutTime.split(':')
        start = [int(start[0]), int(start[1])]
        end = [int(end[0]), int(end[1])]
        
        great = end[1] > start[1]
        st = start[0] == end[0]
        if st and great and abs(start[1] - end[1]) < 15:
            return 0
        while start[1] % 15 != 0:
            start[1] += 1
            if start[1] == 60:
                start[0] += 1
                start[0] %= 24
            start[1] %= 60
            
        while end[1] % 15 != 0:
            end[1] -= 1 
            end[1] %= 60
        

        #print(end[1])
        #print(start[1])
        ediff = abs((int(end[1]) - int(start[1])) // 15)
        
        
        hcount = 0
        while start[0] != end[0] and end[1] >= start[1] or start[0] != ((end[0] - 1) % 24) and end[1] < start[1]:
            start[0] += 1
            start[0] %= 24
            hcount +=1
        
        #print(hcount)
        #print(ediff)
        
        
        res = float('inf')
        if end[1] >= start[1]:
            #add all the hours than check
            res = min(res, hcount * 4 + ediff)
        
        ediff = 0
        #subtract 1 hour than check mins
        
        if start[1] > end[1]:
            while start[1] != end[1]:
                start[1] += 15 
                start[1] %= 60
                ediff +=1

            res = min(res, ((hcount) * 4) + ediff)
        
        return res
        
        
        