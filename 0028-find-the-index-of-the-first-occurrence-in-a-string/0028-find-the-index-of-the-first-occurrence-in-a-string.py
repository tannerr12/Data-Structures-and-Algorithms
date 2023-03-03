class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        lps = [0] * len(needle)
        lis = 0
        i = 1
        
        while i < len(needle):
            
            if needle[lis] == needle[i]:
                
                lps[i] = lis + 1
                lis +=1 
                i+=1
            elif lis == 0:
                lps[i] = 0
                i+=1
            else:
                
                lis = lps[lis-1]

        #haystack
        i = 0
        #needle
        j = 0
        
        while i < len(haystack):
            
            if needle[j] == haystack[i]:
                i+=1
                j+=1
            
            elif j == 0:
                i+=1
            
            else:
                j = lps[j-1]
            
            
            if j >= len(needle):
                return i - len(needle)
        
        return -1
                