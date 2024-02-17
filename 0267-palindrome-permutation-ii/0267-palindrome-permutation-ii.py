class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        ans = []
        c = Counter(s)
        
        def dfs(word):
            
            if len(word) == len(s):
                ans.append(word)
                return
            
            
            for key in c:
                
                if c[key] >= 2:
                    c[key] -= 2
                    dfs(key + word + key)
                    c[key] += 2
                    
            
        
        if len(s) % 2:
            for key in c:
                if c[key] % 2:
                    dfs(key)
        else:
            dfs('')
        
        
        return ans
            
                