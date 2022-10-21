class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        
        h = collections.defaultdict(int)
        h[k] = 1
        total = 0
        temp = 0
        for i in range(len(nums)):
            
            temp += nums[i]
            
            total += h[temp]
            
            h[k + temp] +=1
            
        
        
        return total
        