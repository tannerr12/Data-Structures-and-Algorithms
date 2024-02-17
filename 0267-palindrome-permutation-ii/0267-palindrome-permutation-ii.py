class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        ans = []
        c = Counter(s)
        odd = 0
        for key,val in c.items():
            if len(s) % 2 == 0:
                if val % 2:
                    return []
            else:
                if val % 2:
                    odd += 1
        
        if odd > 1:
            return []
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
            
                