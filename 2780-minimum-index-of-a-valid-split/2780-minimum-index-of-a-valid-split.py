class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        mx = max(c.values())
        
        dom = -1
        for key,val in c.items():
            if val == mx:
                dom = key
                break
        
        
        left = defaultdict(int)
        for i in range(len(nums)):
            
            left[nums[i]] += 1
            c[nums[i]] -= 1
            
            if (left[dom] * 2) > (i + 1) and (c[dom] * 2) > (len(nums) - i - 1):
                return i
        
        return -1
            