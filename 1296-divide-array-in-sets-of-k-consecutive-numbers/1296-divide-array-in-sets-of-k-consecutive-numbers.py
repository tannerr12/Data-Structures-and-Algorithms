class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        nums.sort()
        c = Counter(nums)
        size = 0
        last = 0
        for i in range(len(nums)):
            n = nums[i]
            if c[n] > 0:
                c[n]-=1
                if i != 0 and n-1 > last and size != 0:
                    return False
                size +=1
                size %= k
                last = n
                if c[n] > 0:
                    while c[n] > 0:
                        for j in range(k):
                            if c[n+j] > 0:
                                c[n+j] -=1
                            else:
                                return False
                    
        
        return True if size == 0 else False
                    