class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        vals = []
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                vals.append([arr[i] / arr[j], arr[i], arr[j]])
        
        vals.sort()
 
        return [vals[k-1][1], vals[k-1][2]]
                