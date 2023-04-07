class Solution:
    def originalDigits(self, s: str) -> str:
        #zero, one, two, three, four, five, six, seven, eight, nine
        #Z           w            u     f    x     v      g 
   
        c = Counter(s)
        
        arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
        s = ''
        if c['z'] > 0:
            count = c['z']
            for val in arr[0]:
                c[val] -= count
                    
            s += '0' * count
        
        
        if c['w'] > 0:
            count = c['w']
            for val in arr[2]:
                c[val] -= count
                    
            s += '2' * count
            
        if c['u'] > 0:
            count = c['u']
            for val in arr[4]:
                c[val] -= count
                    
            s += '4' * count
        
        if c['f'] > 0:
            count = c['f']
            for val in arr[5]:
                c[val] -= count
                    
            s += '5' * count
            
        if c['x'] > 0:
            count = c['x']
            for val in arr[6]:
                c[val] -= count
                    
            s += '6' * count
       
        if c['v'] > 0:
            count = c['v']
            for val in arr[7]:
                c[val] -= count
                    
            s += '7' * count
        
        
        if c['g'] > 0:
            count = c['g']
            for val in arr[8]:
                c[val] -= count
                    
            s += '8' * count
        
        
        if c['r'] > 0:
            count = c['r']
            for val in arr[3]:
                c[val] -= count
                    
            s += '3' * count
        
        if c['o'] > 0:
            count = c['o']
            for val in arr[1]:
                c[val] -= count
                    
            s += '1' * count
        
        if c['i'] > 0:
            count = c['i']
            for val in arr[9]:
                c[val] -= count
                    
            s += '9' * count
        
        
        s = sorted(s)
        return ''.join(s)
        
        '''
        while c['o'] > 0 and c['n'] > 0 and c['e'] > 0:
            for val in arr[i]:
                c[val] -=1
                    
            s += str(i)
        '''
        
      
                
            
            
                
            