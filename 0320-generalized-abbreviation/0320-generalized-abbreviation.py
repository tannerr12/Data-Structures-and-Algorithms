class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        
        res = set()
        #mp = {}
        #taken = set()
        def dfs(i, w):
            nonlocal res
            if i >= len(word):
                res.add(w)
                return
            
            for j in range(i, len(word)):
                
                #take character 
                #make sure range is not an abriviation
                wrd = word[i:j+1]
                num = j - i +1
               
                dfs(j+1, w + word[i:j+1])
                
                #convert to number 
                #can only do this if prev is a letter
                if not w or w[-1].isalpha():
                    """
                    if num in mp:
                        if wrd == mp[num]:
                            dfs(j+1, w + str(num))
                        else:
                            continue
                    """    
                    #mp[num] = wrd
                    #taken.add(num)
                    dfs(j+1, w + str(num))
                    #del mp[num]
                    #taken.remove(num)
        
        
        dfs(0,'')
        
        return res
                        
                        
                        