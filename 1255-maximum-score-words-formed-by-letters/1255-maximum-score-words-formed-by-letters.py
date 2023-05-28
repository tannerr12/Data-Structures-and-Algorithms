class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        count = Counter(letters)
        wordls = {}
        
        for word in words:
            wordls[word] = Counter(word)
        
  
        def dfs(i,count):
   
            if i >= len(words):
                return 0
            
            res = 0
            
            #dont do word
            res = max(res, dfs(i+1,count))

            process = True
            sco = 0
            
            for key,val in wordls[words[i]].items():
                sco += val * score[ord(key) - ord('a')]
                if count[key] < val:
                    process = False
                    break
            
            if process:
     
                res = max(res, dfs(i+1,count - wordls[words[i]]) + sco)
                
              
            
            return res
        
        
        return dfs(0,count)