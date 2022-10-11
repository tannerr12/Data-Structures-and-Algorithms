class Solution:
    def simplifyPath(self, path: str) -> str:
        print(path)
        
        stack = []
        i = 0
        while i < len(path):
            
            if not stack and path[i] != '/':
                i+=1
                continue
            
            if path[i] == '/':
                
                i+=1
                
                while i < len(path) and path[i] == '/':
                    i+=1
                    
                
                word = ''
                
                while i < len(path) and path[i] != '/':
                    word += path[i]
                    i+=1
                
                if word == '.':
                    word = ''
                elif word == '..':
                    if stack:
                        stack.pop()
                    word = ''
                if len(word) > 0:
                    stack.append(word)
            
        res = ''
        for val in stack:
            res += '/'
            res += val
        
        return res if len(res) > 0 else "/"