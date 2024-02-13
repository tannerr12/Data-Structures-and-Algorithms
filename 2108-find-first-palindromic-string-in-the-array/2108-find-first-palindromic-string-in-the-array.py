class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def isPali(i):
            l,r = 0, len(words[i])-1
            
            while l < r:
                
                if words[i][l] != words[i][r]:
                    return False
                l+=1
                r-=1
            
            return True
        
        
        for i in range(len(words)):
            if isPali(i):
                return words[i]
        
        return ""