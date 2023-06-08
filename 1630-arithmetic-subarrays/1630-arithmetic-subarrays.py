class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        res = []
        for i in range(len(l)):
            
            newArr = nums[l[i]: r[i]+1]
            
            newArr.sort()
            
            if len(newArr) == 1:
                res.append(True)
                continue
            
            diff = newArr[1] - newArr[0]
            failed = False
            for i in range(1,len(newArr)):
                if newArr[i] - newArr[i-1] != diff:
                    res.append(False)
                    failed = True
                    break
            
            if not failed:
                res.append(True)
        return res