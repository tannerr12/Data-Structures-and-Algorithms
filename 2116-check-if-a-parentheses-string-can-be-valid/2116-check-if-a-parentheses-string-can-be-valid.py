class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        #lock = s.count(')')
        #openleft = s.count('(')
        s = list(s)
        locked = list(locked)
        count = 0
        reserveOp = deque()
        reserveCl = deque()
        result1 = 0
        for i in range(len(s)):
            if locked[i] == "0" and s[i] == ')':
                reserveOp.appendleft(i)                
             
                
            if s[i] == '(':
                count += 1
            else:
                if count <= 0:
                    if len(reserveOp) == 0:
                        return False
                    idx = reserveOp.pop()
                    s[idx] = '('
                    locked[idx] = "1"
                    count += 1
                else:
                    count -= 1
        
        
        if count == 0:
            return True
        count = 0
        for i in range(len(s)-1,-1,-1):
            if locked[i] == "0" and s[i] == '(':
                reserveCl.appendleft(i)                
             
                
            if s[i] == ')':
                count += 1
            else:
                if count <= 0:
                    if len(reserveCl) == 0:
                        return False
                    idx = reserveCl.pop()
                    s[idx] = ')'
                    locked[idx] = "1"
                    count += 1
                else:
                    count -= 1
        
        
        return count == 0