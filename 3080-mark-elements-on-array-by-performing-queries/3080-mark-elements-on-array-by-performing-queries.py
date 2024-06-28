class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        vals = nums.copy()
        total = sum(nums)
        mark = set()
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
            
        
        heapify(nums)
        ans = [0] * len(queries)
        for i in range(len(queries)):
            
            x,y = queries[i]
            
            if x not in mark:
                mark.add(x)
                total -= vals[x] 
            
            while y and nums:
                
                a,b = heappop(nums)
                if b not in mark:
                    mark.add(b)
                    y-=1
                    total -= vals[b]
            
            ans[i] = total
            
        
        
        return ans
                    
            
        