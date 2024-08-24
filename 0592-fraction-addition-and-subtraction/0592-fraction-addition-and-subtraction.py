class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        #add all left numbers * lcm / right
        left = []
        right = []
        signs = []
        
        
        word = ''
        
        
        for i in range(len(expression)):
            
            if expression[i] == '/':
                left.append(int(word))
                word = ''
                
            elif len(word) > 0 and (expression[i] == '+' or expression[i] == '-'):
                right.append(int(word))
                word = ''
                signs.append(expression[i])
            else:
                word += expression[i]
        
        right.append(int(word))
       
            
        
        val = 1
        
        for v in right:
            val = lcm(val, v)
        
        start = left[0] * (val // right[0])
        
        for i in range(1, len(left)):
            cur = left[i] * (val // right[i])
            if signs[i-1] == '+':
                start += cur
            else:
                start -= cur
        
        if start == 0:
            return '0/1'
        
        val2 = gcd(start,val)
        
        start //= val2
        val //= val2
        return str(start) + '/' + str(val)
        print(val)