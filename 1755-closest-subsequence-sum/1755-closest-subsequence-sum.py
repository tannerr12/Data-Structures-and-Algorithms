class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:

        subsets = [0]
        for i in range(len(nums) // 2):
            
            for j in range(len(subsets)):
                
                subsets.append(nums[i] + subsets[j])
            
        subsets.sort()
        
        subsets2 = [0]
        for i in range(len(nums) // 2, len(nums)):
            
            for j in range(len(subsets2)):
                
                subsets2.append(nums[i] + subsets2[j])
            
        subsets2.sort()

    
        l,r = 0,len(subsets2) -1 
        
        while l < len(subsets):
            
            while r > 0 and abs(goal - (subsets2[r-1] + subsets[l])) <= abs(goal- (subsets2[r] + subsets[l])):
                r -= 1
            
            subsets[l] = abs(goal- (subsets2[r] + subsets[l]))
            l+=1
            
        
        
        subsets.sort()
        return subsets[0]