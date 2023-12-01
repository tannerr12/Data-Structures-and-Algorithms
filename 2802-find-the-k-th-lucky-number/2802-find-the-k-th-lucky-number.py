class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        
        
        #4, 7 -> 2
        
        #44,47,74,77 -> 4
        
        #444,474,447,477,744,777,747,774 -> 8
        
        
        n = 2
        count = 2
        pos = 1
        while k > count:
            
            n *= 2
            count += n
            pos += 1
        
        upper = count
        count -= n
        #print(pos)
        
        ans = []
        
        for i in range(pos,0,-1):
            mid = (upper + count) // 2
            if k > mid:
                ans.append("7")
                count = mid
            
            else:
                ans.append("4")
                upper = mid
        
        return ''.join(ans)
                
   
        
        
        
        '''
        def dfs(i, num):
            nonlocal count,ans 
            if i == pos:
                count += 1
                if count == k:
                    ans = num
                return
            #take 4
            dfs(i+1, num * 10 + 4)
            #take 7
            dfs(i+1, num * 10 + 7)
            
        
        
        dfs(0, 0)
        
        return str(ans)
        '''