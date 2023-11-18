
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
        

        du = 0
        dd = 0
        
        sl = [0]
        pref = 0
        res = 0
        for i in range(len(nums)):
            #update(i+1,nums[i])
            pref += nums[i]
            du = pref - upper
            dd = pref - lower

            idx1 = bisect_left(sl, du)
            idx2 = bisect_right(sl, dd)

            res += abs(idx1 - idx2)
            
            
            insort(sl, pref)
        
        #-2,5,-1
        
        #0,-2,3,2
        #  1, 2, 3 
        return res
        #[-2, 0, 3 ] : 2
        #count the occurances between upper and lower bound = 2
        
        #[-2, 0] : 5 = -3, -7
 
        
        