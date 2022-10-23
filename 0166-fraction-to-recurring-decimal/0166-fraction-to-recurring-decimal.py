class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        #if denominator == 1:
         #   return numerator
        
        
        tempN = abs(numerator)
        tempD = abs(denominator)
        
        posCheck = False
        
        if numerator >= 0 and denominator >= 0 or numerator < 0 and denominator < 0:
            posCheck = True
        #return 0
        n = str(tempN)
        i = 0
        carry = 0
        res = ''
        val = ''
        dec = False
        repeat = False
        
        decPos = 0
        memo = {}
        while True:
            
            
            if i >= len(n) and dec == False:
                res += '.'
                dec = True
                #decPos = len(res)
            if i >= len(n):
                
                val = str(carry) + "0"
                
            elif carry > 0:
                val = str(carry)  + n[i]
            else:
                val = n[i]
                
                   
            carry = int(val) % tempD
            
            
            if (carry,val) in memo:
                res+= ")"
                repeat = True
                decPos = memo[(carry,val)] -1
                break
            res += str(int(val) // tempD)
            if i >= len(n):
                memo[(carry,val)] = len(res)
            i+=1
           # while i < len(n) and carry == 0 and int(n[i]) == 0:
           #     res += "0"
           #     i+=1
            if i >= len(n) and carry == 0:
                break
            
            
            
        
        
        #print(res)
        j = 0
        while len(res) > 1 and res[j] == '0' and res[j+1] != '.' and j< len(res) -1:
            j+=1
        
        res = res[j:]
                
        if repeat:
            
            res = res[0:decPos-j] + '(' + res[decPos-j:]

        if (posCheck == False):
            if not (len(res) == 1 and res[0] == '0'):
                res = '-' + res
        return res
            
            
            
            