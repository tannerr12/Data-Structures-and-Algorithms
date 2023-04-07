class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        
        res = []
        
        @cache
        def dfs(i, w):
            nonlocal res
            if i >= len(word):
                res.append(w)
                return
            
            for j in range(i, len(word)):
                
                #take character 
                #make sure range is not an abriviation
                wrd = word[i:j+1]
                num = j - i +1
                
                dfs(j+1, w + wrd)
                
                #convert to number 
                #can only do this if prev is a letter
                if not w or w[-1].isalpha():
                    dfs(j+1, w + str(num))

        dfs(0,'')
        
        return res
                        
                        
                        