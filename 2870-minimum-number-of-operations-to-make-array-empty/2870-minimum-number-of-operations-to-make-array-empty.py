class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp = Counter(nums)
        
        res = 0
        for key,val in mp.items():
            
            if val == 1:
                return -1
            elif val % 3 == 0:
                res += val // 3
            elif val % 3 == 2 or val % 3 == 1:
                res += val // 3
                res += 1
            else:
                return -1
            
        return res