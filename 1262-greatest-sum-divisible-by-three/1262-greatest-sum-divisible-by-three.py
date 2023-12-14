class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        
        mp = defaultdict(list)
        for num in nums:
            mp[num % 3].append(num)
            
        
        
        #print(mp)
        #take all 1s to make the offset 1
        c1 = len(mp[1]) % 3
        c2 = (len(mp[2]) * 2) % 3
        #print(c1)
        #print(c2)
        
        if (c1 + c2) % 3 == 0:
            return sum(mp[1] + mp[2] + mp[0])
        elif (c1 + c2) % 3 == 1:
            p1 = sum(mp[1][1:] + mp[2] + mp[0])
            p2 = sum(mp[1] + mp[2][2:] + mp[0])
            ans = 0
            if len(mp[1]) >= 1:
                ans = max(ans, p1)
            if len(mp[2]) >= 2:
                ans = max(ans, p2)
            return ans
        elif (c1 + c2) % 3 == 2:
            p1 = sum(mp[1][2:] + mp[2] + mp[0])
            p2 = sum(mp[1] + mp[2][1:] + mp[0])
            ans = 0
            if len(mp[1]) >= 2:
                ans = max(ans, p1)
            if len(mp[2]) >= 1:
                ans = max(ans, p2)
            return ans
        else:
            return 0
        #1000
        #1,2,3
        
        #take 1 2 + take 1 1 
        #take 3 1s + 0 2s
        #take 3 2s + 0 1s
        '''
        @cache
        def dfs(i,j):
            
            res = 0
        
            
            #take 1 1 take 1 2
            if i >= 0 and j >= 0:
                res = max(res, dfs(i-1,j-1) + mp[1][i] + mp[2][j])
            
            if i >= 2:
                res = max(res, dfs(i-3, j) + mp[1][i] + mp[1][i-1] + mp[1][i-2])
        
            if j >= 2:
                res = max(res, dfs(i, j-3) + mp[2][j] + mp[2][j-1] + mp[2][j-2])
            
            return res
    
        
        return dfs(len(mp[1])-1, len(mp[2])-1) + sum(mp[0])
        '''