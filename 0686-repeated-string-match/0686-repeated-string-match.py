class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        l,r = len(a),len(b)
        increase = max(1,math.ceil(r / l))
        
        orgA = a
        a = a * increase
       
        
        
        valid = False
        
        for i in range(len(a) - len(b) + 1):
            
            if a[i:i+len(b)] == b:
                valid = True
                break
        
        if valid:
            return increase
        
        a += orgA
        increase += 1
        
        for i in range(len(a) - len(b) + 1):
            
            if a[i:i+len(b)] == b:
                valid = True
                break
        
        if valid:
            return increase 
        
        return -1