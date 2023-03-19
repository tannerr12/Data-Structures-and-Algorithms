class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        temp = []
        s = defaultdict(int)
        nums.sort()
        
      
        def dfs(i):
            
            if i >= len(nums):
            
                if len(temp) > 0:
                    return 1
                return 0
            
            res = 0
            #take
            tar = nums[i] - k
            
            if s[tar] == 0:
                temp.append(nums[i])
                s[nums[i]] +=1
                res += dfs(i+1)
                s[nums[i]] -=1
                temp.pop()
            
            #skip
            res += dfs(i+1)
            return res
        
        return dfs(0)