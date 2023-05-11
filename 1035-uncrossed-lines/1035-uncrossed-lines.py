class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        pos = defaultdict(list)
        
        for i,e in enumerate(nums1):
            pos[e].append(i)
        
        @cache
        def dfs(i, k):
            
            if i >= len(nums2):
                return 0
            
            res = 0
            #dont take
            res = max(res,dfs(i+1,k))
            
            #take it
            if nums2[i] in pos:
                idx = bisect_right(pos[nums2[i]], k)
                if idx < len(pos[nums2[i]]):
                    res = max(res, dfs(i+1, pos[nums2[i]][idx]) + 1)
                    
            
            
            return res
        
        
        return dfs(0,-1)
                    
                
            
        