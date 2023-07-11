class Solution:
    def canChange(self, start: str, target: str) -> bool:
        c1 = Counter(start)
        c2 = Counter(target)
        if c1['L'] != c2['L'] or c1['R'] != c2['R'] or c1['_'] != c2['_']:
            return False
        
        stack = []
        
        for i in range(len(start)):
            
            if start[i] == 'L':
                stack = []
            elif start[i] == 'R':
                stack.append('R')
                
            if target[i] == 'R':
                if not stack:
                    return False
                else:
                    stack.pop()
        
        for i in range(len(start)-1,-1,-1):
            
            if target[i] == 'R':
                stack = []
            elif start[i] == 'L':
                stack.append('L')
                
            if target[i] == 'L':
                if not stack:
                    return False
                else:
                    stack.pop()
        
        return True
        
        
            