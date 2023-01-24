class Solution:
    def minCost(self, nums: List[int], k: int) -> int:

        

        
        @cache
        def divide(i):
            
            if i >= len(nums):
                return 0
        
            
            res = float('inf')
            
            
            count = 0
            h = defaultdict(int)
            for j in range(i,len(nums)):
                h[nums[j]] +=1
                if h[nums[j]] == 2:
                    count +=2
                if h[nums[j]] > 2:
                    count +=1
                res = min(res, count + k + divide(j+1))
            

            return res
        
        return divide(0)