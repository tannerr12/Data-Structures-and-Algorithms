class Solution:
    def longestWord(self, words: List[str]) -> str:
        s = set(words)
        res = ''
        
        for i in range(len(words)):
            valid = True
            for j in range(len(words[i])):
                if words[i][:j+1] not in s:
                    valid = False
                    break
                    
            
            if valid:
                if len(words[i]) == len(res):
                    res = min(res, words[i])
                elif len(words[i]) > len(res):
                    res = words[i]
        return res
        