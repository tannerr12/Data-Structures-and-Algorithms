class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        arr2 = arr.copy()
        arr2.sort()
        cur = 0
        last = -1
        
        mp = defaultdict(int)
        for val in arr2:
            
            if val != last:
                cur += 1
                
            mp[val] = cur
            last = val
            
        
        for i in range(len(arr)):
            arr[i] = mp[arr[i]]
            
        return arr