class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        #anytime our running total can stay >= 0 we should keep it
        #we should also keep track of our biggest negative to remove it from sum when we see a negative
        r = 0
        res = float('-inf')
        pos = False
        mxNeg = float('-inf')
        curmxNeg = 0
        
        left = 0
        right = 0
        for i in range(len(arr)):
            if arr[i] > 0:
                left = i
                break
        
        for i in range(len(arr)-1,-1,-1):
            if arr[i] > 0:
                right = i
                break
        
        for i in range(left, len(arr)):
            
            if arr[i] >= 0:
                r += arr[i]
                pos = True

            else:
                res = max(res,r)
                if arr[i] < curmxNeg:
                    r += curmxNeg
                else:
                    r += arr[i]

                mxNeg = max(arr[i],mxNeg)
              
                
                curmxNeg = min(curmxNeg, arr[i])
                if r + curmxNeg <= 0:
                    r = 0
                    curmxNeg = 0
        
            
            
        
        res = max(res,r)
        r = 0
        curmxNeg = 0
        for i in range(right,-1,-1):
            
            if arr[i] >= 0:
                r += arr[i]
                

            else:
                res = max(res,r)
                if arr[i] < curmxNeg:
                    r += curmxNeg
                else:
                    r += arr[i]

                curmxNeg = min(curmxNeg, arr[i])
                if r + curmxNeg <= 0:
                    r = 0
                    curmxNeg = 0
        
        res = max(res,r)
        r = 0
        curmxNeg = 0
        for i in range(left, len(arr)):
            
            if arr[i] >= 0:
                r += arr[i]
                

            else:
                res = max(res,r)
                if arr[i] < curmxNeg:
                    r += curmxNeg
                else:
                    r += arr[i]

                curmxNeg = min(curmxNeg, arr[i])
                if r <= 0:
                    r = 0
                    curmxNeg = 0
        res = max(res,r)
        r = 0
        curmxNeg = 0
        for i in range(right,-1,-1):
            
            if arr[i] >= 0:
                r += arr[i]
                

            else:
                res = max(res,r)
                if arr[i] < curmxNeg:
                    r += curmxNeg
                else:
                    r += arr[i]

                curmxNeg = min(curmxNeg, arr[i])
                if r <= 0:
                    r = 0
                    curmxNeg = 0
        
        res = max(res,r)
        
        return res if pos else mxNeg