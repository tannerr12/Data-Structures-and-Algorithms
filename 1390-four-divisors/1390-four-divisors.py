class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(len(nums)):
            j = 1
            count = 0
            s = 0
            curr = nums[i]
            while j <= isqrt(nums[i]):
                
                if curr % j == 0:
                    if j == curr // j:
                        count += 1
                    else:
                        count += 2
                        s += curr // j
                    s += j

                j+=1
            if count == 4:
                res += s
        
        
        return res
                    
                