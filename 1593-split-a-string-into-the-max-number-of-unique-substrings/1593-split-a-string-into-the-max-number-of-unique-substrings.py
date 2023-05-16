class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        val = set()

        def dfs(i,word):
            
            if i >= len(s):
                if word not in val:
                    return 1
                else:
                    return float('-inf')
            
            res = 0
            #take
            res = max(res,dfs(i+1, word + s[i]))
            
            #skip
            if word not in val:
                val.add(word)
                res = max(res,dfs(i+1, s[i]) +1)
                val.remove(word)

            return res
        
        return dfs(1, s[0])
  
        