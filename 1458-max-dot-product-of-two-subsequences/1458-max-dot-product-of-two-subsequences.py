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
        def dfs(i, j, take):
            
            if i >= len(nums1) or j >= len(nums2):
                if take:
                    return 0
                else:
                    return float('-inf')
            
            
            res = float('-inf')
            
            #take both
            res = max(res, dfs(i+1, j+1, True) + nums1[i] * nums2[j])
            
            #skip nums1
            res = max(res, dfs(i+1, j, take))
            
            #skip nums2
            res = max(res, dfs(i, j+1, take))            
            
            return res
        
        
        return dfs(0,0,False)
    
        