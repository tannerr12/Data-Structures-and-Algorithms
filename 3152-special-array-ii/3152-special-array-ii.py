class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        prefix = []
        prefix.append(0)
        
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] + (nums[i] % 2 == nums[i-1] % 2))
        
            
        
        ans = []
        for x,y in queries:
            
            dist = y - x
            
            if prefix[y] == prefix[x]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans