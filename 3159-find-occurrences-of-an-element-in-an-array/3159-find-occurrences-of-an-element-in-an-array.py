class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        for i in range(len(queries)):
            queries[i] = (queries[i], i)
        
        
        queries.sort()
        ans = [-1] * len(queries)
        idx = 0
        seen = 0
        for i in range(len(nums)):
            
            if nums[i] == x:
                seen += 1
                
                while idx < len(queries) and seen >= queries[idx][0]:
                    ans[queries[idx][1]] = i
                    idx += 1
            
        
        return ans
                