class Solution:
    def addMinimum(self, word: str) -> int:
        
        stack = []
        mp = {'a':'b', 'b': 'c', 'c': 'a'}
        res = 0
        
        if word[0] == 'b':
            res = 1
        elif word[0] == 'c':
            res = 2
        
        for char in word:
            
            while stack and char != mp[stack[-1]]:
                stack.append(mp[stack[-1]])
                res +=1
                
            stack.append(char)
            
        if stack[-1] == 'a':
            res +=2
        elif stack[-1] == 'b':
            res +=1
        return res
        
        