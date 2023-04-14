class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        res = [0] * 5
        c = Counter(arr)
        great5 = 0
        for key in c:
            if key > 5:
                great5 += c[key]
        #first
        if 2 in c and great5 < 2:
            res[0] = 2
            c[2] -=1
            if c[2] == 0:
                del c[2]
                
        elif 1 in c:
            res[0] = 1
            c[1] -=1
            if c[1] == 0:
                del c[1]
        
        elif 0 in c:
            res[0] =0
            c[0] -=1
            if c[0] == 0:
                del c[0]
        else:
            return ""
        
        
        if res[0] < 2:
            mx = max(c)
            res[1] = mx
            c[mx] -=1
            if c[mx] == 0:
                del c[mx]
        else:    
            if 3 in c:
                res[1] = 3
                c[3] -=1
                if c[3] == 0:
                    del c[3]

            elif 2 in c:
                res[1] = 2
                c[2] -=1
                if c[2] == 0:
                    del c[2]

            elif 1 in c:
                res[1] =1
                c[1] -=1
                if c[1] == 0:
                    del c[1]
            elif 0 in c:
                res[1] =0
                c[0] -=1
                if c[0] == 0:
                    del c[0]
            else:
                return ""
        
        res[2] = ":"
        
        if 5 in c:
            res[3] = 5
            c[5] -=1
            if c[5] == 0:
                del c[5]
                
        elif 4 in c:
            res[3] = 4
            c[4] -=1
            if c[4] == 0:
                del c[4]
        

        elif 3 in c:
            res[3] = 3
            c[3] -=1
            if c[3] == 0:
                del c[3]
                
        elif 2 in c:
            res[3] = 2
            c[2] -=1
            if c[2] == 0:
                del c[2]
        
        elif 1 in c:
            res[3] =1
            c[1] -=1
            if c[1] == 0:
                del c[1]
        elif 0 in c:
            res[3] =0
            c[0] -=1
            if c[0] == 0:
                del c[0]
        else:
            return ""
        
        #print(c)
        for key in c:
            res[4] = key
        
       
        for i in range(len(res)):
            res[i] = str(res[i])
        return ''.join(res)