class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        #anytime our running total can stay >= 0 we should keep it
        #we should also keep track of our biggest negative to remove it from sum when we see a negative
        r = 0
        r2 = 0
        res = float('-inf')
        mxNeg = float('-inf')
        curmxNeg = 0
        curmxNeg2 = 0
        left = float('inf')
        right = -1
        for i in range(len(arr)):
            
            if arr[i] > 0:
                left = min(i, left)
                right = max(i, right)
            else:
                mxNeg = max(arr[i],mxNeg)
        
        if left == float('inf'):
            return mxNeg
    
        
        for i in range(left, len(arr)):
            
            if arr[i] >= 0:
                r += arr[i]
                r2 += arr[i]
                res = max(res,r,r2)

            else:
                res = max(res,r,r2)
                if arr[i] < curmxNeg:
                    r += curmxNeg
                    r2 += curmxNeg2
                else:
                    r += arr[i]
                    r2 += arr[i]
                
                
                curmxNeg = min(curmxNeg, arr[i])
                curmxNeg2 = min(curmxNeg2, arr[i])
                if r + curmxNeg <= 0:
                    r = 0
                    curmxNeg = 0
                if r2 <= 0:
                    r2 = 0
                    curmxNeg2 = 0
        
        r = 0
        r2 = 0
        curmxNeg = 0
        curmxNeg2 = 0
        for i in range(right,-1,-1):
            
            if arr[i] >= 0:
                r += arr[i]
                r2 += arr[i]
                res = max(res,r,r2)
            else:
                res = max(res,r,r2)
                if arr[i] < curmxNeg:
                    r += curmxNeg
                    r2 += curmxNeg2
                else:
                    r += arr[i]
                    r2 += arr[i]

                curmxNeg = min(curmxNeg, arr[i])
                curmxNeg2 = min(curmxNeg2, arr[i])
                if r + curmxNeg <= 0:
                    r = 0
                    curmxNeg = 0
                if r2 <= 0:
                    r2 = 0
                    curmxNeg2 = 0
                
        
        
        return res 