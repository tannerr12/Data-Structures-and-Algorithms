class Solution:
    def stringCount(self, n: int) -> int:
        
        #word either contains non leet character or contains leet character
        #we have 2 cases characters left to place & characters needed 
        #we should multiply our result by number of non leet = 23 if we place a non leet
        #we should multiply our result by leet remaining if leet 3?
        
        #is this 10 ** 5 * 4? 100k positions with only a decision on 4
        #can we early return 26 ** n - i if we run out of options early?
        #can use the leet characters again once they are used up
        MOD = 10 ** 9 + 7
        
        @cache
        def dfs(used, left):
            
            if used == 0:
                return pow(26, left, MOD)
            elif left == 0:
                return used == 0
            
            count = 0
            count += 1 if used & (1 << 1) > 0 or used & (1 << 2) > 0 else 0
            count += 1 if used & (1 << 3) > 0 else 0 
            count += 1 if used & (1 << 0) > 0 else 0

            res = 0
            lused = False
            
            #add a leet character
            if used > 0:
                for i in range(4):
                    if used & (1 << i) > 0:
                        #add an e character
                        if i == 1 or i == 2:
                            if lused:
                                continue
                            lused = True
                        res += (dfs(used ^ (1 << i), left-1)) % MOD
            
            #add generic character
            res += (dfs(used, left-1) * (23 + 3-count)) % MOD
            
            
            return res % MOD
        
        
        return dfs(15, n)
        
        #leet
        #3,2,2,1
        #eelt
        #3,3,2,1
        