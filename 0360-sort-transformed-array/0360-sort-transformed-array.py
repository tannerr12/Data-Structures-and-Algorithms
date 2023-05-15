class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        def quad(x):
            return a * x ** 2 + b * x + c
        
        
        l,r = 0, len(nums)-1
        result = []
        while l <= r:
            
            left,right = quad(nums[l]), quad(nums[r])
            if a >= 0:
                if left > right:
                    result.append(left)
                    l+=1

                else:
                    result.append(right)
                    r -=1
            else:
                
                if left <= right:
                    result.append(left)
                    l+=1

                else:
                    result.append(right)
                    r -=1

        if a >= 0:
            result = result[::-1]
        return result
                
                