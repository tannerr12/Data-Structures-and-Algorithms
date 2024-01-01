class Solution:
    def countInterestingSubarrays(self, nums: List[int], mod: int, k: int) -> int:
        
        acc = 0
        res = 0
        count = defaultdict(int)
        count[0] += 1
        
        for a in nums:
            acc = (acc + (1 if a % mod == k else 0)) % mod
            res += count[(acc - k) % mod]
            count[acc] += 1
            
            
            
        return res
            
            
        