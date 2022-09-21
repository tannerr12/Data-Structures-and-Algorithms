class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        mn, mx = len(str(low)), len(str(high))
        
        res = deque()
        
        s = ''
        for i in range(1,mn +1):
            if i == 10:
                        return res
            s+=str(i)
        if int(s) > high:
            return []
        if int(s) >= low:
            res.append(s)
        while True:
            temp = ''
            increase = False
            for char in s:
                
                if char != '9':
                    val = int(char) +1
                    temp += str(val)
            
                else:
                    increase = True
                    break
            
            if increase:
                r = len(s)
                s= ''
                for i in range(1,r+2):
                    if i == 10:
                        return res
                    s+=str(i)
                
                temp = s
            if int(temp) > high:
                break
            s = temp
            if int(temp) >= low:
                res.append(temp)
            
            
        return res
            
            
            