class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        needle = deque(needle)
       # print(needle)
        s  = deque()
    
        for i in range(len(haystack)):
            s.append(haystack[i])
            
            if len(s) > len(needle):
                s.popleft()
            
            
            if len(s) == len(needle) and s == needle:
                return i - len(s) +1
            
        return -1