class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        #n^4
        
        #take nums1
        
        #take nums2
        
        #take both 
        
        #skip both
        
        #always multiply negatives with eachother // what if the next negative is larger?
        #for each negative compare all other negatives and jump to index
        #dont take individually always take both at once this becomes take both or skip one or the other so counts are always the same
        #n^3
        
        @cache
        def dfs(i, j):
            
            if i >= len(nums1) or j >= len(nums2):
                
                return 0
        
            
            
            res = float('-inf')
            
            #take both
            res = max(res, dfs(i+1, j+1) + nums1[i] * nums2[j])
            
            #skip nums1
            res = max(res, dfs(i+1, j))
            
            #skip nums2
            res = max(res, dfs(i, j+1))            
            
            return res
        
        
        ans = dfs(0,0)
    
        if ans == 0:
            mn1,mx1 = min(nums1), max(nums1)
            mn2,mx2 = min(nums2), max(nums2)
            return max(mx1 * mn2, mx2 * mn1, mx1 * mx2, mn1 * mn2)
        return ans