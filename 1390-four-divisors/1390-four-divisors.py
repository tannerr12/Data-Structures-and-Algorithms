class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(len(nums)):
            j = 1
            count = set()
            s = 0
            curr = nums[i]
            while j <= isqrt(nums[i]) and curr > 1:
                
                if curr % j == 0:
                    s += j
                    count.add(j)
                    s += curr // j
                    count.add(curr//j)
                    #curr //= j
                    
                j+=1
            if len(count) == 4:
                res += s
        
        
        return res
                    
                