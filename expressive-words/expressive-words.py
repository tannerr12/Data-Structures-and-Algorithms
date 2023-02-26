class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        
        
        res = 0
        for i,e in enumerate(words):
            l = 0
            
            i = 0
            while i < len(s) and l < len(e):
                consec = 0
                if e[l] != s[i]:
                    break
                while i < len(s) and e[l] == s[i]:
                    consec +=1
                    i+=1
                
                if consec == 2 and (l == len(e)-1 or e[l] != e[l+1]): #or consec == 1 and e[l] == e[l+1]:
                    i = 0
                    break
                
                else:
                    char = e[l]
                    while l < len(e) and e[l] == char:
                        l+=1
                        consec -=1
                    
                    if consec < 0:
                        i =0
                        break
                
            
            if i >= len(s) and l >= len(e):
                res +=1
        
        return res
        
        
        
        
        
        """
        words = set(words)
        ans = set()
    
        @cache
        def dfs(i, word):
            
            if i >= len(word)-1:
                if word in words:
                    ans.add(word)
            
                return 
            
            
            #remove
            if word[i] == word[i+1] == word[i-1]:
                dfs(i, word[:i] + word[i+1:])
                #dfs(i, word[:i-1] + word[i+1:])
            #dont remove
            dfs(i+1, word)
            
        
        
        dfs(1,s)
        print(ans)
        
        return len(ans)
        """