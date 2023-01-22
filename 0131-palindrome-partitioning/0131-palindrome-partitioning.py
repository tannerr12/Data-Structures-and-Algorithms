class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        res = []
        short = []
        def isPalindrone(temp):
            l,r = 0, len(temp) -1
            
            while l < r:
                if temp[l] != temp[r]:
                    return False
                
                l+=1
                r-=1
            
            return True
        
        
        def backtrack(i):
            
            
            if i >= len(s):
                res.append(short.copy())
                return

            for j in range(i,len(s)):
                
                if isPalindrone(s[i:j+1]):
                    short.append(s[i:j+1])
                    backtrack(j+1)
                    short.pop()
        
        
        backtrack(0)
        
        return res
            