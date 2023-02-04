class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        first = {}
        last = {}
        
        def binary(target):
            l,r = 0, len(prizePositions) -1
            
            while l <= r:
                
                mid = (l+r) //2
                
                if (prizePositions[mid] == target and mid == len(prizePositions) -1):
                    return mid
                
                if  (prizePositions[mid] == target and mid != len(prizePositions) -1 and prizePositions[mid+1] > target):
                    return mid
                
                if (prizePositions[mid] < target and mid == len(prizePositions) -1):
                    return mid
                
                if (prizePositions[mid] < target and mid != len(prizePositions) -1 and prizePositions[mid+1] > target):
                    return mid
                    
                elif prizePositions[mid] > target:
                    r = mid -1
                
                else:
                    l = mid + 1
            
            
            return l
        
        
        for i,num in enumerate(prizePositions):
            
            if num not in first:
                first[num] = i
            
            last[num] = i
            
        
        
    #    print(first)
        #print(last)
        arr = []
        for key,val in first.items():
            
            lastK = binary(key + k)
            
            calc = last[prizePositions[lastK]] - val + 1
            
            arr.append((val,last[prizePositions[lastK]], calc))
        
        
        #print(arr)
        
        arr = sorted(arr, key=lambda x: (x[2]), reverse=True)
        
        #print(arr)
        ans = 0
        for j in range(min(100, len(arr))):
            res = arr[j][2]
            f = arr[j][0]
            l = arr[j][1]

            #print(res)
            #print(arr)
            extra = 0
            for i in range(j + 1,len(arr)):
                val = arr[i][2]

                if arr[i][0] >= f and arr[i][0] <= l and arr[i][1] > l:
                    val = arr[i][1] - l

                elif arr[i][1] >= f and arr[i][1] <= l and arr[i][0] < f:

                    val = f - arr[i][0]

                elif arr[i][0] >= f and arr[i][1] <= l:
                    val = 0

                elif arr[i][0] < f and arr[i][1] > l:
                    val = f - arr[i][0] + arr[i][1] - l

                #print(val)
                extra = max(extra, val)
            
            ans = max(ans,res + extra)
        
        
        return ans
                
            