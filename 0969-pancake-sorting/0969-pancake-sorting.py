class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        flips = []
        
        i = len(arr) -1
        def reverse(l,r):
            
            while l < r:
                
                arr[l],arr[r] = arr[r], arr[l]
                l+=1
                r-=1
            
        while i != 0:
            
            if arr[i] != i+1:
                # find the i + 1
                j = 0
                for x in range(i):
                    if arr[x] == i+1:
                        j = x
                        break
                reverse(0, j)
                flips.append(j+1)
                reverse(0, i)
                flips.append(i+1)
                
            else:
                i-=1
        
        
        #print(arr)
        return flips