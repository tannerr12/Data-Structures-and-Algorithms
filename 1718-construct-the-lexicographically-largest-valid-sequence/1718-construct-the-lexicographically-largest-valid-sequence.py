class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        #maycala
        if n == 1:
            return [1]
        res = [0] * ((n * 2) -1)
        res[0] = n
        res[n] = n
        ans = []
        def dfs(j,used):
            nonlocal ans
            if used == mask:
                if len(ans) == 0:
                    ans = res.copy()
                return
            elif j >= len(res):
                return
            elif len(ans) > 0:
                return
            if res[j] != 0:
                dfs(j+1, used)
            else:
                for i in range(n, 0, -1):
                    if i == 1 or j + i < len(res) and res[j+i] == 0 and used & (1 << i) == 0:
                        if i == 1:
                            res[j] = 1
                            dfs(j+1, used | (1 << i))
                            res[j] = 0
                        else:
                            res[j + i] = i
                            res[j] = i
                            dfs(j+1,used | (1 << i))
                            res[j+i] = 0
                            res[j] = 0
        
        
        mask = (2 ** (n+1)) -1
        mask ^= (1 << 0)
        dfs(1,(1 << n))
        
        
        return ans