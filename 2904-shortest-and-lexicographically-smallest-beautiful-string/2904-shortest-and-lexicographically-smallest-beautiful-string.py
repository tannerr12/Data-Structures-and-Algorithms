class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        arr = []
        arr.append(0)
        for i in range(len(s)):
            if s[i] == "1":
                arr.append(arr[-1] + 1)
            else:
                arr.append(arr[-1])
        
        
        
        
        res = [float('inf'), '']
        for i in range(len(arr)):
            
            if arr[i] >= k:
                
                idx = bisect_right(arr, arr[i] -k)
                if res[0] > i - idx + 1 or (res[0] == i - idx + 1 and res[1] > s[idx-1:i]):
                    res = [i - idx + 1, s[idx-1:i]]
                
        
        return res[1] 
                