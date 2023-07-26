class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        
        odd = []
        even = []
        count = 0
        res = 0
        for i in range(len(nums)):
            
            if nums[i] % 2:
                odd.append(nums[i])
            elif count != k:
                even.append(nums[i])
        
        even.sort()
        odd.sort()
        
        if k % 2:
            if len(even) > 0:
                res += even.pop()
            else:
                return -1
            k-=1
            
        while k:
            if len(even) >= 2 and len(odd) >= 2 and even[-2] + even[-1] >= odd[-2] + odd[-1]:
                res += even.pop()
                res += even.pop()
            elif len(odd) >= 2:
                res += odd.pop()
                res += odd.pop()
            
            elif len(even) >= 2:
                res += even.pop()
                res += even.pop()
            else:
                return -1

            k-=2
        
        return res

        
        