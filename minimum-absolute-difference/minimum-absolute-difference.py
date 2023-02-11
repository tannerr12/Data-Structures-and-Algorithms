class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        
        res = []
        diff = float('inf')
        for i in range(1,len(arr)):
            diff = min(diff, abs(arr[i] - arr[i-1]))
        for i in range(1,len(arr)):
            if abs(arr[i] - arr[i-1]) == diff:
                res.append([arr[i-1],arr[i]])
        
        
        return res