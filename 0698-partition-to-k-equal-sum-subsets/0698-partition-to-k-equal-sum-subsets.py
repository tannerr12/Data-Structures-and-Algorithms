class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = sum(nums)
        if totalSum % k != 0:
            return False
        target = totalSum // k
        group = [0] * k
        nums.sort(reverse=True)
        def backtrack(i,g,bitmask):
            nonlocal target
            if g >= k:
                return True
            
            res = False
            for j in range(i, len(nums)):
                
                if bitmask & (1 << j) ==0 and group[g] + nums[j] <= target:
                    group[g] += nums[j]
                    #take
                    res = res or backtrack(j + 1 if (group[g] != target) else 0,g + (group[g] == target),bitmask | (1<<j))
                    group[g] -= nums[j]
            
            return res
        
        
        g = 0
        bitmask = 0
        if nums[0] > target:
            return False
   
        for i,num in enumerate(nums):
            if num == target:
                bitmask |= (1 << i)
                group[g] = target
                g +=1
        
        for i,num in enumerate(nums):
            if bitmask & (1 << i) == 0:
                group[g] = num
                bitmask |= (1 << i)
                break
        
        return backtrack(0,g,bitmask)
            
                    