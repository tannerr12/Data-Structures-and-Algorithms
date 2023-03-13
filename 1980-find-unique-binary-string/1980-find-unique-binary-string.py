class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        mx = len(nums)
        nums = set(nums)
        ans = ''
        
        @cache
        def dfs(s):
            nonlocal mx
            nonlocal ans
            if len(s) == mx:
                
                if s not in nums:
                    ans = s
                    return True
                return False
            
            res = False
            #add 0 
            res = res or dfs(s + '0')
            
            #add 1
            res = res or dfs(s + '1')
            
            
            return res
        
        
        dfs('')
        return ans