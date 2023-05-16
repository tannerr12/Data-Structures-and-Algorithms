class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        val = defaultdict(int)
        arr = []
        def dfs(i,word):
            
            if i >= len(s):
                if word not in val:
                    return len(arr) + 1
                else:
                    return 0
            
            res = 0
            #take
            res = max(res,dfs(i+1, word + s[i]))
            
            #skip
            if word not in val:
                arr.append(word)
                val[word] +=1
                res = max(res,dfs(i+1, s[i]))
                val[word] -=1
                if val[word] == 0:
                    del val[word]
                arr.pop()
            
            return res
        
        return dfs(1, s[0])
  
        