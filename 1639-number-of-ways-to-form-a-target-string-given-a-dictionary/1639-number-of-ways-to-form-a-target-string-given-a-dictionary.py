class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        
        wordMp = defaultdict(dict)
        for i in range(len(words)):
            
            for j,w in enumerate(words[i]):
                if w in wordMp[j]:
                    wordMp[j][w] += 1
                else:
                    wordMp[j][w] = 1
        
        mx = len(words[0])

        @cache
        def dfs(j, k):
            nonlocal mx
            if k >= len(target):
                return 1
            
            if j >= mx:
                return 0
            
            res = 0
            
            #skip k
            res += dfs(j + 1, k)
            res %= MOD
            if target[k] in wordMp[j]:
                res += wordMp[j][target[k]] * dfs(j + 1, k + 1)
                res %= MOD
                    
            
            return res
        
        
        
        
        return dfs(0,0) % MOD
            