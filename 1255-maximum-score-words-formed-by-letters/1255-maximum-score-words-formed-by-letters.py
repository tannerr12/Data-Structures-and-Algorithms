class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        count = Counter(letters)
        wordls = defaultdict(dict)
        
        for word in words:
            wordls[word] = Counter(word)
        
       
        def dfs(i):
            nonlocal count
            if i >= len(words):
                return 0
            
            res = 0
            
            #dont do word
            res = max(res, dfs(i+1))
            
            c = count
            process = True
            sco = 0
            
            for key,val in wordls[words[i]].items():
                if count[key] < val:
                    process = False
                    break
            
            if process:
                for key,val in wordls[words[i]].items():
                    count[key] -= val
                    sco += score[ord(key) - ord('a')] * val

                res = max(res, dfs(i+1) + sco)
                
                for key,val in wordls[words[i]].items():
                    count[key] += val  


            
            return res
        
        
        return dfs(0)