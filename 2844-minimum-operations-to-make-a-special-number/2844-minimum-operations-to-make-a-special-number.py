class Solution:
    def minimumOperations(self, num: str) -> int:
        
        res = 0
        #25,50,75,100
        has1 = False
        two = []
        seven = []
        five = []
        zero = []
        
        for i in range(len(num)):
            
            if num[i] == '2':
                two.append(i)
            elif num[i] == '5':
                five.append(i)
            elif num[i] == '7':
                seven.append(i)
            elif num[i] == '0':
                zero.append(i)
  
            
        
        has1 = has1 or (len(zero) > 0)
        res = len(num) - has1
        
        if len(seven) > 0 and len(five) > 0:
            idx = bisect_right(seven, five[-1])
            idx -= 1
            if idx >= 0:
                res = min(res,len(num) - five[-1] + five[-1] - seven[idx] - 2)
            
        if len(two) > 0 and len(five) > 0:
            idx = bisect_right(two, five[-1])
            idx -= 1
            if idx >= 0:
                res = min(res,len(num) - five[-1] + five[-1] - two[idx] - 2)
        
        if len(zero) > 0 and len(five) > 0:
            idx = bisect_right(five, zero[-1])
            idx -= 1
            if idx >= 0:
                res = min(res,len(num) - zero[-1] + zero[-1] - five[idx] - 2)
        
        if len(zero) >= 2:
            res = min(res, len(num) - zero[-1] -2 + zero[-1] - zero[-2])
        
        return res 