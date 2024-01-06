class Solution:
    def isNumber(self, s: str) -> bool:
       
        seenE = False
        seenDec = False
        digitsPre = 0
        digitsAft = 0
        digitsAftE = 0
        digitsTotal = 0
        
        nums = set(['0','1','2','3','4','5','6','7','8','9'])
        for i in range(len(s)):
            
            if i == 0 and (s[i] == '+' or s[i] == '-'):
                continue
            
            elif s[i] == '.' and seenDec:
                return False
            elif s[i] == '.' and seenE:
                return False
            elif s[i] == '.':
                seenDec = True
            elif (s[i] == 'E' or s[i] == 'e') and seenE:
                return False
            elif (s[i] == 'E' or s[i] == 'e') and digitsPre + digitsAft == 0:
                return False
            elif s[i] == 'E' or s[i] == 'e':
                seenE = True
            elif (s[i] == '+' or s[i] == '-') and seenE and digitsAftE == 0:
                continue
            elif s[i] in nums:
                if seenDec:
                    digitsAft += 1
                else:
                    digitsPre += 1
                
                if seenE:
                    digitsAftE += 1
                
                digitsTotal += 1
            
            #last case
            elif s[i] not in nums:
                return False
        
        
        if seenE and digitsAftE == 0:
            return False
        elif digitsTotal == 0:
            return False
        
        return True
        