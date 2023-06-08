class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        

        @cache
        def dfs(i, j):
            
            if i == 0:
                return +(j==0)
            #try all of the new songs out j-1 is using a song and n - j + 1 is the number of new songs
            ans = dfs(i-1, j-1) * (n-j+1)
            
            #retry an old song we dont subtract j (songs left - repeat time or 0)
            ans += dfs(i-1, j) * max(j-k,0)
            
            return ans % (10**9+7)
        
        
        return dfs(goal, n)