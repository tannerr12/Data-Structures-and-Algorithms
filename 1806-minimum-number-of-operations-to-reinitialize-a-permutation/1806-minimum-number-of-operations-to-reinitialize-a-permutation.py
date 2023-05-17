class Solution:
    def reinitializePermutation(self, n: int) -> int:
        
        arr = [i for i in range(n)]
        prev = arr.copy()
        #print(arr)
        
        count = 0
        p = False
        while not p:
            p = True
            for i in range(len(arr)):
                if i % 2==0:
                    arr[i] = prev[i//2]
                else:
                    arr[i] = prev[math.floor(n / 2 + (i - 1) / 2)]
                
                if arr[i] != i:
                    p = False
            
            prev = arr.copy()
            
            
            count +=1
            
        
        
        return count
        
        