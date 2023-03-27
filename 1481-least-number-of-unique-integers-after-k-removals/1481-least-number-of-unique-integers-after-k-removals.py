class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        c = Counter(arr)
        
        arr = []
        for key,val in c.items():
            arr.append(val)
            
        arr.sort()
        for i in range(len(arr)):
            k -= arr[i]
            if k <= 0:
                if k == 0:
                    return len(arr) - i - 1
                else:
                    return len(arr) - i
                
            
        
        
        
            