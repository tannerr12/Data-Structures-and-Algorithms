class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        
        mp = defaultdict(int)
        
        
        for i in range(len(target)):
            mp[target[i]] = i
            
        
        newArr = []
        
        for i in range(len(arr)):
            if arr[i] in mp:
                newArr.append(arr[i])
        
        if len(newArr) == 0:
            return len(target)
        #print(newArr)
        
        #3 -> 0
        #<-   2
        # = 2
        cost = defaultdict(int)
        
        idxArr = []
        
        def LDS(newArr):
            
            arr = []
            for i in range(len(newArr)):
                
                idx = bisect_left(arr, mp[newArr[i]])
                
                if idx >= len(arr):
                    arr.append(mp[newArr[i]])
                    
                else:
                    arr[idx] = mp[newArr[i]]
                    
            
            return len(set(arr))
        
        
        
        return len(target) - LDS(newArr)    
            
        

        