class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        
        ans = []
        
        @cache
        def dfs(num,target):
            
            if num > high:
                return
            
            if num == 0:
                for i in range(1,10):
                    if i <= target:
                        dfs(i, target)
            
            else:
                rem = num % 10
                
                if rem + 1 < 10:
                    dfs(num * 10 + rem+1, target)
                if rem - 1 >= 0:
                    dfs(num * 10 + rem-1, target)
                    
            if num >= low and num <= high:
                ans.append(num)
                    
        
        dfs(0,high)
        
        #print(ans)
        
        ans.sort()
        
        return ans