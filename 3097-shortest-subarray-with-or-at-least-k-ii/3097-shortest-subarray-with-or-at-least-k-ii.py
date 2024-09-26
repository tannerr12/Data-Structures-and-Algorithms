class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        
        r = 0
        cur = 0
        best = float('inf')
        bits = defaultdict(int)
        for i in range(len(nums)):
            
            while r < len(nums) and (cur < k or r == i):
                cur |= nums[r]
                for j in range(30):
                    if nums[r] & (1 << j) > 0:
                        bits[j] += 1
            
                r+=1
                
            
            if cur >= k and r > i:
                best = min(best, r - i)
            
            
            for j in range(30):
                if nums[i] & (1 << j) > 0:
                    bits[j] -= 1
                    if bits[j] == 0:
                        cur ^= (1 << j)
            
        
        
        return best if best != float('inf') else -1
                