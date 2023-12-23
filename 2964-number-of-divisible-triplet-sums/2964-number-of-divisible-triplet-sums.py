class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        
        mod = defaultdict(int)
        
        for num in nums:
            mod[num % d] += 1
        
        res = 0
        for i in range(len(nums)):
            mod[nums[i] % d] -= 1
            md = mod.copy()
            for j in range(i + 1, len(nums)):
                md[nums[j] % d] -= 1
                target = d - ((nums[i] % d) + (nums[j] % d))
                target %= d
                
                if md[target] > 0:
                    res += md[target]
        
        return res
                