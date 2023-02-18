class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = 1
        if num < 0:
            sign = -1
            num = num * -1
        base7 = []
        
        n = 0
        while 7 ** n <=num:
            
            base7.append(7**n)
            n+=1
        
        #print(base7)
        res = ''
        for i in range(len(base7)-1,-1,-1):
            count =0 
            while base7[i] <= num:
                num-= base7[i]
                count +=1
            
            res += str(count)
            
        #print(sign)
        return str(int(res) * sign)