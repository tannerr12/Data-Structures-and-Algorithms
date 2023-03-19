class Solution:
    def validIPAddress(self, q: str) -> str:
        ipv4 = False
        if '.' in q:
            ipv4 = True
        
        s = set(['0','1','2','3','4','5','6','7' ,'8','9'])
        alph = set(['a','b','c','d','e','f','A','B','C','D','E','F'])
        if ipv4:
            arr = q.split('.')
            if len(arr) != 4:
                return "Neither"
            
            for val in arr:
                if len(val) == 0 or len(val) > 3 or (len(val) > 1 and val[0] == '0'):
                    return "Neither"
                
                for char in val:
                    if char not in s:
                        return "Neither" 
                
                num = int(val)
                
                if num >255:
                    return "Neither"
                    
            
            return "IPv4"
        else:
            
            arr = q.split(':')
            
            if len(arr) != 8:
                return "Neither"
            
            for val in arr:
                if len(val) == 0 or len(val) > 4:
                    return "Neither"
                for char in val:
                    if char in s or char in alph:
                        continue
                    else:
                        return "Neither"
            
            return "IPv6"
            
            
            
            