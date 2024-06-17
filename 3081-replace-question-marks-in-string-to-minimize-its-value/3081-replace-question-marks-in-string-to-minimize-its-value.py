class Solution:
    def minimizeStringValue(self, s: str) -> str:
        
        alpha = [0] * 26
        for char in s:
            if char != '?':
                pos = ord(char) - ord('a')
                alpha[pos] += 1
        ans = []    
        for char in s:
            
            if char == '?':
                mn = min(alpha)
                for i in range(len(alpha)):
                    if alpha[i] == mn:
                        alpha[i] += 1
                        ans.append(chr(i + ord('a')))
                        break

                                   
        
        
        ans.sort(reverse=True)
        
        res = []
        
        for val in s:
            if val == '?':
                res.append(ans.pop())
            
            else:
                res.append(val)
        
        return ''.join(res)
                          
